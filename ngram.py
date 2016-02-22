import itertools
import math
import os
import re
import sys

import nltk
import numpy
from scipy.optimize import fmin_slsqp


class NGram:
    class WordDictionary:
        def __init__(self):
            self.word_dict = {}
            self.words_in_dict = 0

        def get_probability(self, word):
            if self.words_in_dict == 0:
                return 0

            return self.word_dict.get(word, 0) / self.words_in_dict

        def increase_count(self, word):
            self.word_dict[word] = self.word_dict.get(word, 0) + 1
            self.words_in_dict += 1

        def __iter__(self):
            return self.word_dict.__iter__()

        def keys(self):
            return self.word_dict.keys()

    def __init__(self):
        self.ngrams = {}
        self.unigrams = {}
        self.word_count = 0

        self.probabilities = []

    @classmethod
    def train_model(cls, sentences, order=((1, 0), (2, 0), (3, 0))):
        print('Pruning Unknowns')
        sentences = prune_unknowns(sentences)

        ngram = NGram()

        print('Unknowns Pruned. Gramifying and Training.')

        def corpus_grams():
            for sent in sentences:
                for model in order:
                    yield from cls.get_ngrams(sent, *model)

        ngram.train(corpus_grams())
        return ngram

    @staticmethod
    def get_ngrams(sequence, n, k):
        if n == 1 and k == 0:
            for word in sequence:
                yield (word,)
        else:
            for ngram in nltk.ngrams(sequence, n + k, pad_right=True):
                head = ngram[:1]
                tail = ngram[1:]
                for skip_tail in itertools.combinations(tail, n - 1):
                    if skip_tail[-1] is None:
                        continue
                    yield head + skip_tail

    def train(self, grams):
        for i, gram in enumerate(grams):
            if len(gram) == 1:
                self.unigrams[gram[0]] = self.unigrams.get(gram[0], 0) + 1
                self.word_count += 1
            else:
                self.add(gram)

    def add(self, ngram):
        prefix = ngram[:-1]
        word = ngram[-1]

        prefix_dict = self.ngrams.get(prefix, NGram.WordDictionary())
        prefix_dict.increase_count(word)

        self.ngrams[prefix] = prefix_dict

    def successor_probabilities(self, prefix):
        prefix = tuple(word if word in self.unigrams else '<UNK>' for word in prefix)

        bigrams = dict([(word, self.ngrams[prefix[-2:]].get_probability(word))
                        for word in self.ngrams[prefix[-2:]].keys()]) if prefix[-2:] in self.ngrams else {}

        trigrams = dict([(word, self.ngrams[prefix].get_probability(word))
                         for word in self.ngrams[prefix].keys()]) if prefix in self.ngrams else {}

        potentials = [word for word in list(bigrams.keys()) + list(trigrams.keys())]

        word_probabilities = {word: (bigrams.get(word, 0), trigrams.get(word, 0)) for word in potentials}

        return word_probabilities

    """
    Given a list of sentences, will set self.probabilities to a list of tuples with the predictive probabilities for the
    unigram, bigram, and trigram models
    """

    def sentences_probabilities(self, sentences, orders=((1, 0), (2, 0), (3, 0))):
        self.probabilities.clear()
        for sentence in sentences:
            sentence_probabilities = ()

            for order in orders:
                order_probabilities = []

                for gram in self.get_ngrams(sentence, *order):
                    if len(gram) == 1:
                        order_probabilities.append(
                            self.unigrams.get(gram[0], self.unigrams['<UNK>']) / self.word_count, )
                    else:
                        prefix = gram[:-1]
                        value = gram[-1]

                        order_probabilities.append(self.ngrams[prefix].get_probability(value)
                                                   if prefix in self.ngrams else 0, )
                sentence_probabilities += (order_probabilities,)

            self.probabilities.append(list(zip(*sentence_probabilities)))

    """
    Interpolate together the unigram, bigram, and trigram probabilities
    :return: the resulting list of lists of interpolated probabilities for each word in each sentence
    """

    def interpolate(self, lambdas):

        lambda_sum = sum(lambdas)

        if lambda_sum == 0:
            lambdas = (0,) * len(lambdas)
        else:
            lambdas = [weight / lambda_sum for weight in lambdas]

        for sentence in self.probabilities:
            sentence_probs = []
            for word in sentence:
                sentence_probs.append(sum([p * w for p, w in zip(word, lambdas)]))
            yield sentence_probs

    """
    Compute models perplexity after interpolating with the given lambdas
    :returns: the average perplexity of this model evaluated across all sentences, a list of perplexity values for each sentence
    """

    def perplexity(self, lambdas):

        lambdas = tuple(lambdas)
        sentence_perplexities = []

        for sentence in self.interpolate(lambdas):

            word_perplexities = []
            for word_probability in sentence:
                if word_probability > 0.0:
                    word_perplexities.append(-1 * math.log2(word_probability))
                else:
                    word_perplexities.append(float('inf'))

            sentence_perplexities.append(math.pow(2, sum(word_perplexities) / len(word_perplexities)))

        return sum(sentence_perplexities) / len(sentence_perplexities), sentence_perplexities


def get_unknowns(word_counts, k):
    return set(word for word, count in word_counts.items() if count <= k)


def get_word_histogram(sentences):
    word_counts = {}
    for sentence in sentences:
        for word in sentence:
            word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts


def prune_unknowns(sentences, k=1):
    sentences = list(sentences)

    word_hist = get_word_histogram(sentences)
    unknowns = get_unknowns(word_hist, k)
    yield from [[word if word not in unknowns else '<UNK>' for word in sentence] for sentence in sentences]


def optimize_lambdas(model, initial_guess, bounds=None):
    if not bounds:
        bounds = (1,) * len(initial_guess)

    def opt_func(weights):
        return model.perplexity(tuple([a * b for a, b in zip(weights, bounds)]))[0]

    parameters = fmin_slsqp(func=opt_func,
                            x0=numpy.asarray(initial_guess),
                            bounds=[(0, 1)] * len(initial_guess),
                            disp=False,
                            full_output=False,
                            epsilon=.1)

    parameters = tuple([a * b for a, b in zip(parameters, bounds)])

    return parameters


def get_sentences(untokenized_text, is_tokenized=False, sentence_tokenizer=None, token_start_end=None):
    if not is_tokenized:
        yield from [('<s0> <s1> ' + sentence + ' </s>').split()
                    for sentence in sentence_tokenizer(untokenized_text) if sentence]
    else:
        start_token, end_token = token_start_end
        yield from [('<s0> <s1> ' + sentence + '</s>').split()
                    for sentence in re.findall(r'{}(.*){}'.format(start_token, end_token), untokenized_text) if
                    sentence]


def main():
    if len(sys.argv) != 5:
        print('Error parsing command line arguments, please use the following')
        print('\tngram.py <1|2|2s|3|3s> <trainfile> <devfile> <testfile>')
        return

    model_type, train_path, dev_path, test_path = sys.argv[1:]

    with open(train_path, 'r') as train_file:
        train_sentences = get_sentences(untokenized_text=train_file.read().rstrip(),
                                        is_tokenized=False,
                                        sentence_tokenizer=lambda text: [sentence for sentence in text.split('.')])

    # Train on test sentences

    ngram = NGram.train_model(train_sentences)
    del train_sentences

    with open(dev_path, 'r') as dev_file:
        dev_sentences = get_sentences(untokenized_text=dev_file.read().rstrip(),
                                      is_tokenized=True,
                                      token_start_end=('<s>', '</s>'))

    # Compute probabilities for dev_file
    ngram.sentences_probabilities(dev_sentences)
    del dev_sentences

    # Optimize lambdas for interpolation
    lambdas = optimize_lambdas(ngram, initial_guess=(1, 1, 1), bounds={'1': (1, 0, 0),
                                                                       '2': (0, 1, 0),
                                                                       '2s': (1, 1, 0),
                                                                       '3': (0, 0, 1),
                                                                       '3s': (1, 1, 1)}[model_type])

    with open(test_path, 'r') as test_file:
        test_sentences = get_sentences(untokenized_text=test_file.read().rstrip(),
                                       is_tokenized=True,
                                       token_start_end=('<s>', '</s>'))

    # Computing probabilities for test_file
    test_sentences = list(test_sentences)
    ngram.sentences_probabilities(test_sentences)

    average_perplexity, sentences_perplexity = ngram.perplexity(lambdas=lambdas)

    test_sentences = [' '.join(sentence).replace('<s0> <s1>', '<s>') for sentence in test_sentences]
    print('Average perplexity over all sentences: {0:.5f} using the following lambdas: {1}'.format(average_perplexity,
                                                                                                   lambdas))

    for i, sentence_perplexity in enumerate(sentences_perplexity):
        print('{0:.5f} : {1}'.format(sentence_perplexity, test_sentences[i]))


if __name__ == '__main__':
    main()

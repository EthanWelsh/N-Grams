import math
import re
import sys

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

    def train(self, sentences, n, disp=False):
        if n == 1:
            for i, sentence in enumerate(sentences):
                if disp and int((i / len(sentences)) * 100) % 2 == 0:
                    progress = int((i / len(sentences)) * 100)
                    self.progress_bar(progress)

                for word in sentence:
                    self.unigrams[word] = self.unigrams.get(word, 0) + 1
                    self.word_count += 1

        else:
            for i, sentence in enumerate(sentences):
                if disp and int((i / len(sentences)) * 100) % 2 == 0:
                    progress = int((i / len(sentences)) * 100)
                    self.progress_bar(progress)

                for ngram in zip(*[sentence[i:] for i in range(n)]):
                    self.add(ngram)

        if disp:
            self.progress_bar(100)
            print()

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

    def sentences_probabilities(self, sentences, disp=False):
        self.probabilities.clear()

        for i, sentence in enumerate(sentences):
            if disp and int((i / len(sentences)) * 100) % 2 == 0:
                progress = int((i / len(sentences)) * 100)
                self.progress_bar(progress)

            sentence_probabilities = []

            for trigram in zip(*[sentence[i:] for i in range(3)]):
                trigram = tuple(word if word in self.unigrams else '<UNK>' for word in trigram)

                unigram_prob = self.unigrams.get(trigram[-1], self.unigrams['<UNK>']) / self.word_count
                bigram_prob, trigram_prob = 0, 0

                if trigram[-2] in self.ngrams:
                    bigram_prob = self.ngrams[trigram[-2]].get_probability(trigram[-1])

                if trigram[-3:-1] in self.ngrams:
                    trigram_prob = self.ngrams[trigram[-3:-1]].get_probability(trigram[-1])

                sentence_probabilities += [(unigram_prob, bigram_prob, trigram_prob)]

            self.probabilities += [sentence_probabilities]

        if disp:
            self.progress_bar(100)
            print()

    """
    Interpolate together the unigram, bigram, and trigram probabilities
    :return: the resulting list of lists of interpolated probabilities for each word in each sentence
    """

    def interpolate(self, lambdas):

        w1, w2, w3 = lambdas
        lambda_sum = sum(lambdas)
        lambdas = (w1 / lambda_sum, w2 / lambda_sum, w3 / lambda_sum) if lambda_sum > 0 else (0, 0, 0)

        interpolated_probabilities = []
        for sentence in self.probabilities:
            sentence_probs = []
            for word in sentence:
                sentence_probs.append(sum([p * w for p, w in zip(word, lambdas)]))
            interpolated_probabilities += [sentence_probs]

        return interpolated_probabilities

    """
    Compute models perplexity after iteroplating with the given lambdas
    :returns: the average perplexity of this model evaluated across all sentences, a list of perplexity values for each sentence
    """

    def perplexity(self, lambdas):

        lambdas = tuple(lambdas)
        sentence_perplexities = []
        for sentence in self.interpolate(lambdas):

            word_perplexities = []
            for word_probability in sentence:
                if word_probability > 0.0:
                    word_perplexities += [-1 * math.log2(word_probability)]
                else:
                    word_perplexities += [float('inf')]

            sentence_perplexities += [math.pow(2, sum(word_perplexities) / len(word_perplexities))]

        return sum(sentence_perplexities) / len(sentence_perplexities), sentence_perplexities

    @staticmethod
    def progress_bar(progress):
        sys.stdout.write('\r[{0}] {1}%'.format('#' * progress + ' ' * (100 - progress), progress))
        sys.stdout.flush()


def get_unknowns(word_counts, k):
    return set(word for word, count in word_counts.items() if count <= k)


def get_word_histogram(sentences):
    word_counts = {}
    for sentence in sentences:
        for word in sentence:
            word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts


def prune_unknowns(sentences, k=1):
    word_hist = get_word_histogram(sentences)
    unknowns = get_unknowns(word_hist, k)
    return [[word if word not in unknowns else '<UNK>' for word in sentence] for sentence in sentences]


def train_corpus(sentences):
    sentences = prune_unknowns(sentences)
    ngram = NGram()

    ngram.train(sentences, 1)  # unigram
    ngram.train(sentences, 2)  # bigram
    ngram.train(sentences, 3)  # trigram

    return ngram


def optimize_lambdas(model, bounds=((0, 1), (0, 1), (0, 1))):
    parameters = fmin_slsqp(lambda x: model.perplexity(x)[0],
                            (1, 1, 1),
                            bounds=bounds,
                            disp=False,
                            full_output=False,
                            epsilon=.1)

    return tuple(parameters)


def get_sentences(untokenized_text, is_tokenized=False, sent_tokenizer=None, token_start_end=None):
    if not is_tokenized:
        untokenized_text = untokenized_text.lower()
        return [('<s0> <s1> ' + sentence + ' </s>').split()
                for sentence in sent_tokenizer(untokenized_text) if sentence]
    else:
        start_token, end_token = token_start_end
        return [('<s0> <s1> ' + sentence + '</s>').split()
                for sentence in re.findall(r'{}(.*){}'.format(start_token, end_token), untokenized_text) if sentence]


def main():
    if len(sys.argv) != 5:
        print('Error parsing command line arguments, please use the following')
        print('\tngram.py <1|2|2s|3|3s> <trainfile> <devfile> <testfile>')
        return

    model_type, train_path, dev_path, test_path = sys.argv[1:]

    with open(train_path, 'r') as train_file:
        train_sentences = get_sentences(untokenized_text=train_file.read().rstrip(),
                                        is_tokenized=False,
                                        sent_tokenizer=lambda text: [sentence for sentence in text.split('.')])

    with open(dev_path, 'r') as dev_file:
        dev_sentences = get_sentences(untokenized_text=dev_file.read().rstrip(),
                                      is_tokenized=True,
                                      token_start_end=('<s>', '</s>'))

    with open(test_path, 'r') as test_file:
        test_sentences = get_sentences(untokenized_text=test_file.read().rstrip(),
                                       is_tokenized=True,
                                       token_start_end=('<s>', '</s>'))

    # Train on test sentences
    ngram = train_corpus(train_sentences)

    # Compute probabilities for dev_file
    ngram.sentences_probabilities(dev_sentences)

    # Optimize lambdas for interpolation
    lambdas = optimize_lambdas(ngram, bounds={'1':  ((0, 1), (0, 0), (0, 0)),
                                              '2':  ((0, 0), (0, 1), (0, 0)),
                                              '2s': ((0, 1), (0, 1), (0, 0)),
                                              '3':  ((0, 0), (0, 0), (0, 1)),
                                              '3s': ((0, 1), (0, 1), (0, 1))}[model_type])

    # Computing probabilities for test_file
    ngram.sentences_probabilities(test_sentences)

    average_perplexity, sentences_perplexity = ngram.perplexity(lambdas=lambdas)

    print('Average perplexity over all sentences: {0:.5f} using the following lambdas: {1}'.format(average_perplexity, lambdas))
    for i, sentence_perplexity in enumerate(sentences_perplexity):
        print('{0:.5f} : {1}'.format(sentence_perplexity, test_sentences[i]))


if __name__ == '__main__':
    main()

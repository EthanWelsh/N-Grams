import math

import sys


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
                if disp and int((i/len(sentences)) * 100) % 2 == 0:
                    progress = int((i/len(sentences)) * 100)
                    self.progress_bar(progress)

                for word in sentence:
                    self.unigrams[word] = self.unigrams.get(word, 0) + 1
                    self.word_count += 1

        else:
            for i, sentence in enumerate(sentences):
                if disp and int((i/len(sentences)) * 100) % 2 == 0:
                    progress = int((i/len(sentences)) * 100)
                    self.progress_bar(progress)

                for ngram in zip(*[sentence[i:] for i in range(n)]):
                    self.add(ngram)

        if disp:
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
            if disp and int((i/len(sentences)) * 100) % 2 == 0:
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
            print()

    """
    Interpolate together the unigram, bigram, and trigram probabilities
    :return: the resulting list of lists of interpolated probabilities for each word in each sentence
    """

    def interpolate(self, lambdas):
        w1, w2, w3 = lambdas
        lambdas = (w1 / sum(lambdas), w2 / sum(lambdas), w3 / sum(lambdas))

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
            for word_probability in sentence:
                sentence_perplexities += [sum(
                    [math.pow(2,
                              -1 * math.log(word_probability, 2) if word_probability > 0.0 else float('inf'))]) / len(
                    sentence)]

        return sum(sentence_perplexities) / len(sentence_perplexities), sentence_perplexities

    @staticmethod
    def progress_bar(progress):
            sys.stdout.write('\r[{0}] {1}%'.format('#'*progress + ' '*(100-progress), progress))
            sys.stdout.flush()

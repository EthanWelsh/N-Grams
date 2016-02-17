import math


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

    def train(self, sentences, n):
        if n == 1:
            for sentence in sentences:
                for word in sentence:
                    self.unigrams[word] = self.unigrams.get(word, 0) + 1
                    self.word_count += 1

        else:
            for sentence in sentences:
                for ngram in zip(*[sentence[i:] for i in range(n)]):
                    self.add(ngram)

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

    def sentences_probabilities(self, sentences):
        print('Getting probabilities for', len(sentences), 'sentences')
        self.probabilities.clear()
        for sentence in sentences:
            self.probabilities += [self._per_word_probabilities(sentence)]

            # self.probabilities = [self._per_word_probabilities(sentence) for sentence in sentences]

    """
    Given a sentence (a list of words), will compute the probability values for each word in the sentence
    :return: a list of probability values for each respective word of the sentence.
    """

    def _per_word_probabilities(self, sentence):
        probabilities = []

        for trigram in zip(*[sentence[i:] for i in range(3)]):
            prefix, result = (trigram[:2], trigram[-1])

            probabilities += [(self.unigrams.get(result, self.unigrams['<UNK>']) / self.word_count,) +
                              self.successor_probabilities(prefix).get(result, (0, 0))]
        return probabilities

    """
    Interpolate together the unigram, bigram, and trigram probabilities
    :return: the resulting list of lists of interpolated probabilities for each word in each sentence
    """

    def interpolate(self, lambdas):
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

        sentence_perplexities = []
        for sentence in self.interpolate(lambdas):
            for word_probability in sentence:
                sentence_perplexities += [sum(
                    [math.pow(2, -1 * math.log(word_probability, 2) if word_probability > 0.0 else float('inf'))]) / len(
                    sentence)]

        return sum(sentence_perplexities) / len(sentence_perplexities), sentence_perplexities

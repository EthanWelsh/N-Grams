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

    def successor_probabilities(self, prefix, interpolation_weights=(.1, .4, .5)):

        prefix = tuple(word if word in self.unigrams else '<UNK>' for word in prefix)

        unigrams = dict([(word, self.unigrams[word] / self.word_count)
                         for word in self.unigrams.keys()])

        bigrams = dict([(word, self.ngrams[prefix[-2:]].get_probability(word))
                        for word in self.ngrams[prefix[-2:]].keys()]) if prefix[-2:] in self.ngrams else {}

        trigrams = dict([(word, self.ngrams[prefix].get_probability(word))
                         for word in self.ngrams[prefix].keys()]) if prefix in self.ngrams else {}

        unigram_weight, bigram_weight, trigram_weight = interpolation_weights
        normalization_factor = sum(interpolation_weights)

        word_probabilities = {word: (unigram_weight / normalization_factor * unigrams.get(word, 0) +
                                     bigram_weight / normalization_factor * bigrams.get(word, 0) +
                                     trigram_weight / normalization_factor * trigrams.get(word, 0))
                              for word in self.unigrams.keys()}

        return word_probabilities

    def max_successor(self, prefix):
        word_probabilities = self.successor_probabilities(prefix)

        max_word = max(iter(word_probabilities), key=word_probabilities.get)
        return max_word

    def perplexity(self, sentences, lambdas):
        perplexity = 0
        for sentence in sentences:
            perplexity_values = []
            for trigram in zip(*[sentence[i:] for i in range(3)]):
                prefix, result = (trigram[:2], trigram[-1])
                perplexity_values += [self.successor_probabilities(prefix, interpolation_weights=tuple(lambdas)).get(result, 0)]

            print(perplexity_values)
            perplexity += math.pow(2, sum([(-p * math.log(p) if p > 0 else 0) for p in perplexity_values]))

        return perplexity / len(sentences)

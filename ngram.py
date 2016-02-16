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

    def successor_probabilities(self, prefix):
        prefix = tuple(word if word in self.unigrams else '<UNK>' for word in prefix)

        unigrams = dict([(word, self.unigrams[word] / self.word_count)
                         for word in self.unigrams.keys()])

        bigrams = dict([(word, self.ngrams[prefix[-2:]].get_probability(word))
                        for word in self.ngrams[prefix[-2:]].keys()]) if prefix[-2:] in self.ngrams else {}

        trigrams = dict([(word, self.ngrams[prefix].get_probability(word))
                         for word in self.ngrams[prefix].keys()]) if prefix in self.ngrams else {}

        word_probabilities = {word: (unigrams.get(word, 0), bigrams.get(word, 0), trigrams.get(word, 0))
                              for word in self.unigrams.keys()}

        return word_probabilities

    def sentences_probabilities(self, sentences):
        return [self.per_word_probabilities(sentence) for sentence in sentences]

    def per_word_probabilities(self, sentence):
        probabilities = []
        for trigram in zip(*[sentence[i:] for i in range(3)]):
            prefix, result = (trigram[:2], trigram[-1])
            probabilities += [self.successor_probabilities(prefix).get(result, (0, 0, 0))]
        return probabilities

    def interpolate_sentences(self, sentences_probabilities, lambdas):
        return [self._interpolate_sentence(sent, lambdas) for sent in sentences_probabilities]

    @staticmethod
    def _interpolate_sentence(sentence_probabilities, lambdas):
        sentence_probs = []

        for word_probabilities in sentence_probabilities:
            unigram, bigram, trigram = word_probabilities
            unigram_weight, bigram_weight, trigram_weight = lambdas

            assert(sum(lambdas) == 1)

            sentence_probs += [unigram * unigram_weight + bigram * bigram_weight + trigram * trigram_weight]

        return sentence_probs #sum(sentence_probs) / len(sentence_probs)

    def sentences_perplexity(self, sentences_probabilities):
        sentence_perplexity = [self.per_word_perplexity(p) for p in sentences_probabilities]
        return sum(sentence_perplexity) / len(sentence_perplexity)

    @staticmethod
    def per_word_perplexity(sentence_probabilities):
        word_perplexities = [math.pow(2, math.log(p) / len(sentence_probabilities)) if p > 0 else float('inf') for p in sentence_probabilities]
        return sum(word_perplexities) / len(word_perplexities)

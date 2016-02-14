import os
import pickle
import re
from os import listdir
from os.path import isfile, join

import time
from nltk.tokenize import sent_tokenize


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

        word_probabilities = {word: (.1 * unigrams.get(word, 0) +
                                     .4 * bigrams.get(word, 0) +
                                     .5 * trigrams.get(word, 0))
                              for word in self.unigrams.keys()}

        return word_probabilities

    def max_successor(self, prefix):
        word_probabilities = self.successor_probabilities(prefix)

        max_word = max(iter(word_probabilities), key=word_probabilities.get)
        return max_word


def get_sentences(untokenized_text):
    untokenized_text = untokenized_text.lower()
    return [('<s0> <s1> ' + sentence + ' </s>').split() for sentence in sent_tokenize(untokenized_text)]


def get_unknowns(word_counts, k):
    return set(word for word, count in word_counts.items() if count <= k)


def get_word_histogram(sentences):
    word_counts = {}
    for sentence in sentences:
        for word in sentence:
            word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts


def prune_unknowns(sentences):
    word_hist = get_word_histogram(sentences)
    unknowns = get_unknowns(word_hist, 1)
    return [[word if word not in unknowns else '<UNK>' for word in sentence] for sentence in sentences]


def remove_gutenberg_disclamer(file_str):
    disclaimer_regex = r'\*?END\*?THE SMALL PRINT!.*\n?.*\*?END\*?'
    if re.match(disclaimer_regex, file_str):
        return re.split(disclaimer_regex, file_str)[1]

    return file_str


def train_corpus(directory_path, clean_routine=None):
    files = [join(directory_path, file) for file in listdir(directory_path) if isfile(join(directory_path, file))]

    print('Reading in {} files...'.format(len(files)))
    sentences = []
    for file in files:
        print(file)
        with open(file, encoding='utf-8', errors='ignore') as data_file:
            file_data = data_file.read()
            sentences += get_sentences(clean_routine(file_data) if clean_routine else file_data)

    print('Pruning Sentences')
    sentences = prune_unknowns(sentences)

    ngram = NGram()

    print('Training Unigram')
    ngram.train(sentences, 1)  # unigram

    print('Training Bigram')
    ngram.train(sentences, 2)  # bigram

    print('Training Trigram')
    ngram.train(sentences, 3)  # trigram

    return ngram


def main():
    ngram = train_corpus('dev_data', remove_gutenberg_disclamer)

    while True:
        print('>', end=' ')
        words = tuple(input().split())
        print(ngram.max_successor(words))


if __name__ == '__main__':
    main()

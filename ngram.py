import os
import pickle
import re
import sys
from os import listdir
from os.path import isfile, join

from nltk.tokenize import sent_tokenize


class NGram:
    def __init__(self, n):
        self.gram = {}
        self.n = n

    def train(self, sentences):
        for sentence in sentences:
            for ngram in zip(*[sentence[i:] for i in range(self.n)]):
                self.add(ngram)

    def add(self, ngram):
        assert (len(ngram) == self.n)

        if self.n == 1:
            self.gram[ngram] = self.gram.get(ngram, 0) + 1
        else:
            prefix = ngram[:-1]
            word = ngram[-1]

            prefix_dict = self.gram.get(prefix, {})
            prefix_dict[word] = prefix_dict.get(word, 0) + 1

            self.gram[prefix] = prefix_dict

    def get_prefix_dict(self, prefix):
        assert (len(prefix) == self.n - 1)
        return self.gram[prefix]

    def get_most_likely(self, prefix, options=None):
        assert (len(prefix) == self.n - 1)
        prefix_dict = self.get_prefix_dict(prefix)
        return max(iter(options) if options else iter(prefix_dict), key=prefix_dict.get)


def get_sentences(untokenized_text):
    untokenized_text = untokenized_text.lower()
    return [('<s0> <s1> ' + sentence + ' </s>').split() for sentence in sent_tokenize(untokenized_text)]


def train_corpus(directory_path, n):
    ngram = NGram(n)
    disclaimer_regex = r'\*?END\*?THE SMALL PRINT!.*\n?.*\*?END\*?'

    files = [file for file in listdir(directory_path) if isfile(join(directory_path, file))]
    for file in files:
        print(file)
        with open(os.path.join(directory_path, file), encoding='utf-8', errors='ignore') as data_file:
            sentences = get_sentences(re.split(disclaimer_regex, data_file.read())[1])
            ngram.train(sentences)

    return ngram


def main():
    n = int(sys.argv[1])

    ngram_file = '{}gram.pickle'.format(n)
    if os.path.exists(ngram_file):
        print('Reading model from file.')
        with open(ngram_file, 'rb') as handle:
            ngram = pickle.load(handle)
    else:
        ngram = train_corpus('Holmes_Training_Data', n)
        with open(ngram_file, 'wb') as handle:
            pickle.dump(ngram, handle)

    while True:
        print('>', end=' ')
        words = tuple(input().split())
        print(ngram.get_most_likely(words))


if __name__ == '__main__':
    main()

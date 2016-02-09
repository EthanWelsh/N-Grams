import os
import re

import pickle
from nltk.tokenize import sent_tokenize
from os import listdir
from os.path import isfile, join

class NGram:
    def __init__(self, n):
        self.gram = {}
        self.n = n

    def train(self, sentences):
        for sentence in sentences:
            for ngram in zip(*[sentence[i:] for i in range(self.n)]):
                self.add(ngram)

    def add(self, ngram):
        assert(len(ngram) == self.n)

        if self.n == 1:
            self.gram[ngram] = self.gram.get(ngram, 0) + 1
        else:
            prefix = ngram[:-1]
            word = ngram[-1]

            prefix_dict = self.gram.get(prefix, {})
            prefix_dict[word] = prefix_dict.get(word, 0) + 1

            self.gram[prefix] = prefix_dict

    def get_prefix_dict(self, prefix):
        assert(len(prefix) == self.n - 1)
        return self.gram[prefix]

    def get_most_likely(self, prefix, options=None):
        assert(len(prefix) == self.n - 1)
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
    ngram_file = 'ngram.pickle'
    if os.path.exists(ngram_file):
        print('Reading model from file.')
        with open(ngram_file, 'rb') as handle:
            ngram = pickle.load(handle)
    else:
        ngram = train_corpus('/Users/welshej/Downloads/Holmes_Training_Data', 2)
        with open(ngram_file, 'wb') as handle:
            pickle.dump(ngram, handle)

    print('<s1>: ', ngram.get_most_likely(('<s1>',)))
    print('the: ', ngram.get_most_likely(('the',)))
    print('who: ', ngram.get_most_likely(('who',)))
    print('what: ', ngram.get_most_likely(('what',)))
    print('where: ', ngram.get_most_likely(('where',)))
    print('when: ', ngram.get_most_likely(('when',)))


if __name__ == '__main__':
    main()

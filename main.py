import re
from os import listdir
from os.path import isfile, join

import numpy as np
import scipy
from nltk.tokenize import sent_tokenize

from ngram import NGram


def get_sentences(untokenized_text, is_tokenized=False, token_start_end=None):
    if not is_tokenized:
        untokenized_text = untokenized_text.lower()
        return [('<s0> <s1> ' + sentence + ' </s>').split() for sentence in sent_tokenize(untokenized_text)]
    else:
        start_token, end_token = token_start_end
        return [('<s0> <s1> ' + sentence + '</s>').split() for sentence in
                re.findall(r'{}(.*){}'.format(start_token, end_token), untokenized_text)]


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


def remove_gutenberg_disclamer(file_str):
    disclaimer_regex = r'\*?END\*?THE SMALL PRINT!.*\n?.*\*?END\*?'
    if re.match(disclaimer_regex, file_str):
        return re.split(disclaimer_regex, file_str)[1]

    return file_str


def read_corpus(path, is_directory=False, is_tokenized=False, token_start_end=None, clean_routine=None):
    sentences = []

    if is_directory:
        files = [join(path, file) for file in listdir(path) if isfile(join(path, file))]
        print('Reading in {} files...'.format(len(files)))

        for file in files:
            print(file)
            with open(file, encoding='utf-8', errors='ignore') as data_file:
                file_data = data_file.read()
                data_file.readlines()

                sentences += get_sentences(clean_routine(file_data) if clean_routine else file_data, is_tokenized,
                                           token_start_end)
    else:
        with open(path, encoding='utf-8', errors='ignore') as data_file:
            file_data = data_file.read()
            sentences += get_sentences(clean_routine(file_data) if clean_routine else file_data, is_tokenized,
                                       token_start_end)

    return sentences


def train_corpus(sentences):
    sentences = prune_unknowns(sentences)
    ngram = NGram()

    print('Training Unigram')
    ngram.train(sentences, 1)  # unigram

    print('Training Bigram')
    ngram.train(sentences, 2)  # bigram

    print('Training Trigram')
    ngram.train(sentences, 3)  # trigram

    return ngram


def prompt(ngram):
    while True:
        print('>', end=' ')
        words = tuple(input().split())
        print(ngram.max_successor(words))


def optimize_lambdas(model, sentences):
    print('starting optimization')
    parameters = scipy.optimize.minimize(lambda x, s: model.perplexity(lambdas=tuple(x), sentences=s),
                                         np.array([.1, .4, .5]),
                                         args=(sentences,),
                                         options={'disp': False, 'maxiter': 10, 'maxfun':1},
                                         bounds=[(0, 1), (0, 1), (0, 1)])
    print('--------------------------------')
    print(tuple(parameters.x))
    print('--------------------------------')
    return tuple(parameters.x)


def main():
    #train_sentences = read_corpus('train.txt', is_directory=False, is_tokenized=False)

    train_sentences = read_corpus('train_data', is_directory=True, is_tokenized=False)
    #test_sentences = read_corpus('test_data', is_directory=True, is_tokenized=False)

    print('Training on Corpus')
    ngram = train_corpus(train_sentences)

    sentences_probabilities = ngram.sentences_probabilities(train_sentences)

    interpolated_probabilities = ngram.interpolate_sentences(sentences_probabilities, lambdas=(.15, .35, .5))
    print(ngram.sentences_perplexity(interpolated_probabilities))

    interpolated_probabilities = ngram.interpolate_sentences(sentences_probabilities, lambdas=(.1, .3, .6))
    print(ngram.sentences_perplexity(interpolated_probabilities))


    #print('Optimizing Lambdas for Interpolation')
    #lambdas = optimize_lambdas(ngram, train_sentences)
    #print(lambdas)

    #print(ngram.perplexity(sentences=train_sentences, lambdas=lambdas))


if __name__ == '__main__':
    main()

import os
import re
import sys
from os import listdir
from os.path import isfile, join

from nltk.tokenize import sent_tokenize
from scipy.optimize import fmin_slsqp

from ngram import NGram


def remove_gutenberg_disclamer(file_str):
    disclaimer_regex = r'\*?END\*?THE SMALL PRINT!.*\n?.*\*?END\*?'
    if re.match(disclaimer_regex, file_str):
        return re.split(disclaimer_regex, file_str)[1]

    return file_str


def read_corpus(path, is_tokenized=False, token_start_end=None, clean_routine=None, disp=False):
    sentences = []

    if os.path.isdir(path):
        files = [join(path, file) for file in listdir(path) if isfile(join(path, file))]
        for i, file in enumerate(files):
            if disp and int((i / len(files)) * 100) % 2 == 0:
                progress = int((i / len(files)) * 100)
                progress_bar(progress)

            with open(file, encoding='utf-8', errors='ignore') as data_file:
                file_data = data_file.read()
                data_file.readlines()

                sentences += get_sentences(clean_routine(file_data) if clean_routine else file_data, is_tokenized,
                                           token_start_end)

        if disp:
            progress_bar(100)
            print()
    else:
        with open(path, encoding='utf-8', errors='ignore') as data_file:
            file_data = data_file.read()
            sentences += get_sentences(clean_routine(file_data) if clean_routine else file_data, is_tokenized,
                                       token_start_end)

    return sentences


def evaluate(perplexities):
    non_inf_values = []

    for perplexity in perplexities:
        if perplexity != float('inf'):
            non_inf_values += [perplexity]

    return sum(non_inf_values) / len(non_inf_values), len(perplexities) - len(non_inf_values)


def progress_bar(progress):
    sys.stdout.write('\r[{0}] {1}%'.format('#' * progress + ' ' * (100 - progress), progress))
    sys.stdout.flush()


def main():
    #  train_sentences = read_corpus('train.txt', is_directory=False, is_tokenized=False)

    print("Reading Corpus:")
    train_sentences = read_corpus('train_data', is_tokenized=False, disp=True)
    dev_sentences = read_corpus('dev_data', is_tokenized=False, disp=True)
    test_sentences = read_corpus('test_data', is_tokenized=False, disp=True)

    print('\nTraining on Corpus')
    ngram = train_corpus(train_sentences)

    print('\nComputing Probabilities:')
    ngram.sentences_probabilities(dev_sentences, disp=True)

    del train_sentences, dev_sentences

    print('Optimizing Lambdas for Interpolation')
    lambdas = optimize_lambdas(ngram)

    print('Optimization Complete. Optimal interpolation weights:', lambdas)

    print('lambdas={}'.format(lambdas))
    _, sentence_perplexities = ngram.perplexity(lambdas=lambdas)
    print('avg_perplexity: {0:.10f} \t inf_count: {1:.10f}'.format(*evaluate(sentence_perplexities)))

    ngram.sentences_probabilities(test_sentences, disp=True)
    print('Perplexity:', ngram.perplexity(lambdas))


if __name__ == '__main__':
    main()

import re
import sys
import time
from os import listdir
from os.path import isfile, join

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


def read_corpus(path, is_directory=False, is_tokenized=False, token_start_end=None, clean_routine=None, disp=False):
    sentences = []

    if is_directory:
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
            print()
    else:
        with open(path, encoding='utf-8', errors='ignore') as data_file:
            file_data = data_file.read()
            sentences += get_sentences(clean_routine(file_data) if clean_routine else file_data, is_tokenized,
                                       token_start_end)

    return sentences


def train_corpus(sentences):
    sentences = prune_unknowns(sentences)
    ngram = NGram()

    print('\nTraining Unigram')
    ngram.train(sentences, 1, disp=True)  # unigram

    print('\nTraining Bigram')
    ngram.train(sentences, 2, disp=True)  # bigram

    print('\nTraining Trigram')
    ngram.train(sentences, 3, disp=True)  # trigram

    return ngram


def prompt(ngram):
    while True:
        print('>', end=' ')
        words = tuple(input().split())
        print(ngram.max_successor(words))


def optimize_lambdas(model):
    parameters = scipy.optimize.fmin_slsqp(lambda x : model.perplexity(x)[0],
                                           (.1, .4, .5),
                                           bounds=((0, 1), (0, 1), (0, 1)),
                                           disp=False,
                                           full_output=False)

    return tuple(parameters)


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
    #train_sentences = read_corpus('train.txt', is_directory=False, is_tokenized=False)

    print("Reading Corpus:")
    train_sentences = read_corpus('train_data', is_directory=True, is_tokenized=False, disp=True)
    dev_sentences = read_corpus('dev_data', is_directory=True, is_tokenized=False, disp=True)
    #test_sentences = read_corpus('test_data', is_directory=True, is_tokenized=False)

    print('\nTraining on Corpus')
    ngram = train_corpus(train_sentences)

    print('\nComputing Probabilities:')
    ngram.sentences_probabilities(dev_sentences, disp=True)

    del train_sentences, dev_sentences

    print()

    print('lambdas=(.15, .35, .5)')
    _, sentence_perplexities = ngram.perplexity(lambdas=(.15, .35, .5))
    print('avg_perplexity: {0:.10f} \t inf_count: {1:.10f}'.format(*evaluate(sentence_perplexities)))

    print()

    print('lambdas=(.1, .3, .6)')
    _, sentence_perplexities = ngram.perplexity(lambdas=(.1, .3, .6))
    print('avg_perplexity: {0:.10f} \t inf_count: {1:.10f}'.format(*evaluate(sentence_perplexities)))

    print()

    print('Optimizing Lambdas for Interpolation')
    lambdas = optimize_lambdas(ngram)

    print()

    print('lambdas={}'.format(lambdas))
    _, sentence_perplexities = ngram.perplexity(lambdas=lambdas)
    print('avg_perplexity: {0:.10f} \t inf_count: {1:.10f}'.format(*evaluate(sentence_perplexities)))

    # print(ngram.perplexity(sentences=train_sentences, lambdas=lambdas))


if __name__ == '__main__':
    main()

import os
import re
import sys
from os import listdir
from os.path import isfile, join

import itertools
from nltk.tokenize import sent_tokenize

from ngram import NGram, get_sentences, optimize_lambdas


def remove_gutenberg_disclamer(file_str):
    disclaimer_regex = r'\*?END\*?THE SMALL PRINT!.*\n?.*\*?END\*?'
    if re.match(disclaimer_regex, file_str):
        return re.split(disclaimer_regex, file_str)[1]

    return file_str


def read_corpus(path):
    if os.path.isdir(path):
        files = [join(path, file) for file in listdir(path) if isfile(join(path, file))]
        for i, file in enumerate(files):
            with open(file, encoding='utf-8', errors='ignore') as data_file:
                yield from get_sentences(data_file.read().lower(), sentence_tokenizer=sent_tokenize)


def evaluate(perplexities):
    non_inf_values = []

    for perplexity in perplexities:
        if perplexity != float('inf'):
            non_inf_values.append(perplexity)

    return sum(non_inf_values) / len(non_inf_values), len(perplexities) - len(non_inf_values)


def main():
    questions_path, answers_path = sys.argv[1:]

    print("Reading Corpus:")
    train_sentences = read_corpus('train_data')
    model_orders = ((1, 0), (2, 0), (3, 1))

    print('\nTraining on Corpus')

    model = NGram.train_model(train_sentences, order=model_orders)
    del train_sentences

    print('Reading answers')
    with open(answers_path, 'r') as answer_file:
        answers = get_sentences(untokenized_text=answer_file.read(),
                                is_tokenized=True,
                                token_start_end=('<s>', '</s>'))

    dev_sentences = list(answers)[:520]

    print('Calculating Probabilities for Dev Sentences:')
    model.sentences_probabilities(dev_sentences)
    lambdas = optimize_lambdas(model, initial_guess=((1,) * len(model_orders)))
    print('Lambdas:', lambdas)

    with open(questions_path, 'r') as question_file:
        questions = get_sentences(untokenized_text=question_file.read(),
                                  is_tokenized=True,
                                  token_start_end=('<s>', '</s>'))

    print('Calculating Probabilities for Test Sentences:')

    questions = list(questions)
    model.sentences_probabilities(sentences=questions)
    _, sentences_perplexity = model.perplexity(lambdas=lambdas)

    print('Writing sentences and perplexities to file')
    with open('output.txt', 'w') as out_file:
        for i, perplexity in enumerate(sentences_perplexity):
            out_file.write('{}\t{}\n'.format(' '.join(questions[i]).replace('<s0> <s1>', '<s>'), perplexity))


if __name__ == '__main__':
    main()

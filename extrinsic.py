import os
import re
import sys
from os import listdir
from os.path import isfile, join

from nltk.tokenize import sent_tokenize

from ngram import NGram, get_sentences, optimize_lambdas


def remove_gutenberg_disclamer(file_str):
    disclaimer_regex = r'\*?END\*?THE SMALL PRINT!.*\n?.*\*?END\*?'
    if re.match(disclaimer_regex, file_str):
        return re.split(disclaimer_regex, file_str)[1]

    return file_str


def read_corpus(path, disp=False):
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

                sentences += get_sentences(file_data, sentence_tokenizer=sent_tokenize)

        if disp:
            progress_bar(100)
            print()

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
    questions_path, answers_path = sys.argv[1:]

    print("Reading Corpus:")
    train_sentences = read_corpus('train_data', disp=True)

    print('\nTraining on Corpus')
    model = NGram.train_model(train_sentences, disp=True)

    with open(answers_path, 'r') as answer_file:
        answers = get_sentences(untokenized_text=answer_file.read(),
                                is_tokenized=True,
                                token_start_end=('<s>', '</s>'))

    dev_sentences = answers[:520]

    print('Calculating Probabilities for Dev Sentences:')
    model.sentences_probabilities(dev_sentences, disp=True)
    lambdas = optimize_lambdas(model)

    with open(questions_path, 'r') as question_file:
        questions = get_sentences(untokenized_text=question_file.read(),
                                  is_tokenized=True,
                                  token_start_end=('<s>', '</s>'))

    print('Calculating Probabilities for Test Sentences:')
    model.sentences_probabilities(sentences=questions, disp=True)
    _, sentences_perplexity = model.perplexity(lambdas=lambdas)

    print('Writing sentences and perplexities to file')
    with open('output.txt', 'w') as out_file:
        for i, perplexity in enumerate(sentences_perplexity):
            out_file.write('{}\t{}\n'.format(' '.join(questions[i]).replace('<s0> <s1>', '<s>'), perplexity))


if __name__ == '__main__':
    main()

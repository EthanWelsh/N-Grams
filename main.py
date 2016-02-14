import re
from os import listdir
from os.path import isfile, join

from nltk.tokenize import sent_tokenize

from ngram import NGram


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

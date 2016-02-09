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


def main():
    bigram = NGram(2)

    sentences = get_sentences('the cat jumped on the other cat. How was your day? My name is cat, what is yours Mr. Crouch?')
    bigram.train(sentences)
    print(bigram.get_most_likely(('the',)))

if __name__ == '__main__':
    main()

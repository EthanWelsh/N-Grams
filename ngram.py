import operator


class NGram:
    def __init__(self, n):
        self.gram = {}
        self.n = n

    def add(self, words):
        if self.n == 1:
            self.gram[words] = self.gram.get(words, 0) + 1
        else:
            prefix = words[:-1]
            word = words[-1]

            prefix_dict = self.gram.get(prefix, {})
            prefix_dict[word] = prefix_dict.get(word, 0) + 1

    def get_prefix_dict(self, prefix):
        return self.gram[prefix]

    def get_most_likely(self, prefix, options=None):
        prefix_dict = self.get_prefix_dict(prefix)
        return max(iter(options) if options else iter(prefix_dict), key=prefix_dict.get)


def main():
    pass


if __name__ == '__main__':
    main()

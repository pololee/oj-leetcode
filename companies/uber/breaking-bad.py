class TrieNode:
    def __init__(self):
        self.word = None
        self.children = dict()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        word = word.lower()

        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

        node.word = word

    def findWord(self, word):
        word = word.lower()

        node = self.root
        for ch in word:
            if ch not in node.children:
                return False

            node = node.children[ch]

        return node.word is not None

    def startWith(self, prefix):
        prefix = prefix.lower()

        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False

            node = node.children[ch]

        return True


def main():
    trie = Trie()
    trie.insert('word')
    print(trie.findWord('word'))
    print(trie.startWith('wor'))


if __name__ == '__main__':
    main()

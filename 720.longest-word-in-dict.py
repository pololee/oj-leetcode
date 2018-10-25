import unittest


class TrieNode:
    def __init__(self):
        self.wordTilHere = None
        self.table = dict()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node.table:
                node.table[ch] = TrieNode()
            node = node.table[ch]

        node.wordTilHere = word

    def contains(self, word):
        node = self.root

        for ch in word:
            if ch not in node.table:
                return False
            node = node.table[ch]

        return node.wordTilHere is not None


class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        trie = self.buildTrie(words)

        ans = ['']
        self.dfs(trie.root, True, ans)
        return ans[0]

    def dfs(self, trieNode, isRoot, ans):
        if not isRoot and trieNode.wordTilHere is None:
            return

        if trieNode.wordTilHere:
            word = trieNode.wordTilHere
            if len(word) > len(ans[0]) or (len(word) == len(ans[0]) and word < ans[0]):
                ans[0] = word

        for key in trieNode.table:
            self.dfs(trieNode.table[key], False, ans)

    def longestWordWithStack(self, words):
        trie = self.buildTrie(words)

        ans = ''
        stack = [trie.root]

        while stack:
            node = stack.pop()
            if node.wordTilHere is None and node != trie.root:
                continue

            if node.wordTilHere:
                word = node.wordTilHere
                if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                    ans = word

            for ch in node.table:
                stack.append(node.table[ch])

        return ans

    def buildTrie(self, words):
        trie = Trie()
        for word in words:
            trie.insert(word)

        return trie


class TestSoluton(unittest.TestCase):
    def testTrie(self):
        trie = Trie()

        trie.insert("ape")
        trie.insert("apple")
        trie.insert("cable")
        trie.insert("car")
        trie.insert("cart")
        trie.insert("cat")
        trie.insert("cattle")
        trie.insert("curl")
        trie.insert("far")
        trie.insert("farm")

        self.assertTrue(trie.contains('ape'))
        self.assertTrue(trie.contains('apple'))
        self.assertTrue(trie.contains('farm'))
        self.assertFalse(trie.contains('farmm'))

    def testLongestWord(self):
        sol = Solution()
        self.assertEqual(
            'world',
            sol.longestWord(["w", "wo", "wor", "worl", "world"])
        )
        self.assertEqual(
            'world',
            sol.longestWordWithStack(["w", "wo", "wor", "worl", "world"])
        )


if __name__ == '__main__':
    unittest.main()

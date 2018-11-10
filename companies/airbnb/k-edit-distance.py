import unittest


class TrieNode:
    def __init__(self):
        self.table = dict()
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if word == "":
            self.root.word = ""
            return
        node = self.root

        for ch in word:
            if ch not in node.table:
                node.table[ch] = TrieNode()
            node = node.table[ch]

        node.word = word


class Solution:
    def kEditDistance(self, words, target, k):
        if not words:
            return []
        
        trie = Trie()
        for word in words:
            trie.insert(word)

        ans = []
        size = len(target)
        curr = [i for i in range(size + 1)]
        self.kEditDistanceUtil(curr, trie.root, target, k, ans)
        return ans

    def kEditDistanceUtil(self, prev, trieNode, target, k, ans):
        size = len(target)
        if trieNode.word is not None:
            if prev[size] <= k:
                ans.append(trieNode.word)

        for ch in trieNode.table:
            curr = [0 for _ in range(size + 1)]
            curr[0] = prev[0] + 1

            for i in range(1, size + 1):
                if ch == target[i-1]:
                    curr[i] = prev[i-1]
                else:
                    curr[i] = 1 + min(curr[i-1], prev[i], prev[i-1])

            self.kEditDistanceUtil(curr, trieNode.table[ch], target, k, ans)

class SolutionTest(unittest.TestCase):
    def testKEditDistance(self):
        sol = Solution()
        words = ["abcd", "abc", "abd", "ad", "c", "cc"]
        target = "abcd"
        k = 2
        self.assertCountEqual(['abc', 'abcd', 'abd', 'ad'],
                              sol.kEditDistance(words, target, k))
        words = ["as", "ab", "cf", "da", "ee", "e", "adee", "eeda"]
        target = "eefab"
        k = 3
        self.assertCountEqual(["ab", "ee", "eeda"], sol.kEditDistance(words, target, k))

unittest.main()

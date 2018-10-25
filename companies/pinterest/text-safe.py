# 问了一道识别text是否safe。 假设有一个black list, 里面有一些phrase,
# 比如["machine guns", "world war i"],
# 再给一个输入的pintext，
# 如果pintext里有完整的phrase, 就判断为unsafe.
# 注意，"i love world war i"是unsafe的，但"world war ii"是safe的，
# 因为是以word为单位match的
import unittest

class TrieNode:
    def __init__(self):
        self.table = dict()
        self.phraseEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertPhrase(self, phrase):
        node = self.root
        words = phrase.split(' ')

        for word in words:
            if word not in node.table:
                node.table[word] = TrieNode()
            node = node.table[word]

        node.phraseEnd = True

    def search(self, words):
        node = self.root

        for word in words:
            if node.phraseEnd:
                return True
            if word not in node.table:
                return False
            node = node.table[word]
        return node.phraseEnd


class Solution:
    def isSafe(self, blackList, pintext):
        if not blackList or not pintext:
            return True
        
        trie = Trie()
        for phrase in blackList:
            trie.insertPhrase(phrase)
        
        pintextWords = pintext.split(" ")
        for i in range(len(pintextWords)):
            if trie.search(pintextWords[i:]):
                return False
        return True

class SolutionTest(unittest.TestCase):
    def testIsSafe(self):
        sol = Solution()
        blackList = ["machine guns", "world war i"]
        self.assertFalse(sol.isSafe(blackList, "i love world war i"))
        self.assertTrue(sol.isSafe(blackList, "world war ii"))

if __name__=='__main__':
    unittest.main()

import collections
import string


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        wordList.add(beginWord)
        wordList.add(endWord)
        distance, neighbors = self.bfs(beginWord, endWord, wordList)

        ans = []
        self.dfs(beginWord, endWord, ans, [beginWord], distance, neighbors)
        return ans

    def bfs(self, beginWord, endWord, wordList):
        queue = collections.deque()
        distance = {}
        queue.append(endWord)  # start from end word
        distance[endWord] = 0

        neighbors = collections.defaultdict(set)

        while queue:
            word = queue.popleft()

            for neigh in self.getNextWords(word, wordList):
                neighbors[neigh].add(word)

                if neigh in distance:
                    continue
                distance[neigh] = distance[word] + 1
                queue.append(neigh)

        return distance, neighbors

    def dfs(self, beginWord, endWord, paths, sofar, distance, neighbors):
        if len(sofar) > 1 and sofar[-1] == endWord:
            paths.append(list(sofar))
            return

        last = sofar[-1]
        for neigh in neighbors[last]:
            if distance[neigh] != distance[last] - 1:
                continue

            sofar.append(neigh)
            self.dfs(beginWord, endWord, paths, sofar, distance, neighbors)
            sofar.pop()

    def getNextWords(self, word, wordList):
        ans = []

        for i in range(len(word)):
            left = word[:i]
            right = word[i+1:]

            for ch in string.ascii_lowercase:
                if ch == word[i]:
                    continue
                newWord = "{}{}{}".format(left, ch, right)
                if newWord in wordList:
                    ans.append(newWord)
        return ans

import unittest

class SolutionTest(unittest.TestCase):
    def testLadders(self):
        start = "hit"
        end = "cog"
        words = ["hot", "dot", "dog", "lot", "log"]
        sol = Solution()
        print(sol.findLadders(start, end, words))

unittest.main()

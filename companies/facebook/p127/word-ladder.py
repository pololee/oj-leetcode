from collections import deque
import string

class Solution:
    def ladderLength(self, start, end, dictionary):
        if start == end:
            return 0
        
        dictionary.add(end)
        queue = deque()
        visited = set()

        queue.append(start)
        visited.add(start)
        level = 1

        while queue:
            size = len(queue)

            for _ in range(size):
                word = queue.popleft()
                if word == end:
                    return level
                
                for w in self.getNextWords(word):
                    if w not in dictionary or w in visited:
                        continue
                    queue.append(w)
                    visited.add(w)
            level += 1

        return 0
    
    def getNextWords(self, word):
        words = []
        for i in range(len(word)):
            left = word[:i]
            right = word[i+1:]

            for ch in string.ascii_lowercase:
                if word[i] == ch:
                    continue
                words.append("{}{}{}".format(left, ch, right))
        return words

import unittest

class SolutionTest(unittest.TestCase):
    def testLadderLength(self):
        start = "hit"
        end = "cog"
        words = set(["hot", "dot", "dog", "lot", "log"])
        sol = Solution()
        self.assertEqual(5, sol.ladderLength(start, end, words))

unittest.main()

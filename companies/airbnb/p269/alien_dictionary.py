import heapq
import unittest


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alienOrder(self, words):
        # Write your code here
        if not words:
            return ""

        adjTable = self.buildAdjTable(words)
        return self.topologicalSort(adjTable)

    def buildAdjTable(self, words):
        table = dict()
        for word in words:
            for ch in word:
                if ch not in table:
                    table[ch] = set()

        size = len(words)
        for i in range(size - 1):
            currW = words[i]
            nextW = words[i+1]

            for j in range(min(len(currW), len(nextW))):
                if currW[j] != nextW[j]:
                    table[currW[j]].add(nextW[j])
                    break
        return table

    def buildIndegrees(self, adjTable):
        indegrees = dict()
        for key in adjTable:
            indegrees[key] = 0

        for key in adjTable:
            for neigh in adjTable[key]:
                indegrees[neigh] += 1
        return indegrees

    def topologicalSort(self, adjTable):
        indegrees = self.buildIndegrees(adjTable)
        queue = []

        # why heapq?
        # Because "sorted lexicographically by the rules of this new language"
        # If two char same order, then it need to be sorted lexicographically
        for ch in indegrees:
            if indegrees[ch] == 0:
                heapq.heappush(queue, ch)

        ans = []
        while queue:
            node = heapq.heappop(queue)
            ans.append(node)

            for neigh in adjTable[node]:
                indegrees[neigh] -= 1
                if indegrees[neigh] == 0:
                    heapq.heappush(queue, neigh)

        if len(ans) == len(indegrees):
            return ''.join(ans)
        return ""


class SolutionTest(unittest.TestCase):
    def testAlien(self):
        sol = Solution()
        test = ["wrt", "wrf", "er", "ett", "rftt"]
        self.assertEqual('wertf', sol.alienOrder(test))
        test = ['zx', 'zy']
        self.assertEqual('xyz', sol.alienOrder(test))


unittest.main()

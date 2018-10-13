import sys
from collections import deque
import unittest

class Solution:
    def minCost(self, knownWizards):
        # 10 wizards
        # find the min cost between 0 and 9
        minCost = [sys.maxsize for _ in range(10)]
        minCost[0] = 0
        
        queue = deque()
        queue.append(0)
        while queue:
            curr = queue.popleft()

            for knownW in knownWizards[curr]:
                cost = minCost[curr] + self.wizardCost(curr, knownW)
                if cost < minCost[knownW]:
                    minCost[knownW] = cost
                    queue.append(knownW)
        
        return minCost[9]
    
    def wizardCost(self, i, j):
        return (i - j) ** 2

class SolutionTest(unittest.TestCase):
    sol = Solution()

    def testMinCost(self):
        test = [[] for _ in range(10)]
        test[0] = [1, 4, 5]
        test[4] = [9]
        self.assertEqual(41, self.sol.minCost(test))

if __name__=='__main__':
    unittest.main()

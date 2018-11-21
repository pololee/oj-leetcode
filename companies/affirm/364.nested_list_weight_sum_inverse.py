# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

from collections import deque


class Solution:
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        totalSum = 0
        prevLevelSum = 0
        queue = deque()
        for x in nestedList:
            queue.append(x)

        while queue:
            size = len(queue)

            levelSum = 0
            for _ in range(size):
                x = queue.popleft()
                if x.isInteger():
                    levelSum += x.getInteger()
                else:
                    for y in x.getList():
                        queue.append(y)
            prevLevelSum += levelSum
            totalSum += prevLevelSum
        return totalSum
    
    def depthSumInverseAgain(self, nestedList):
        return self.depthSumInverseAgainHelper(nestedList, 0)
    
    def depthSumInverseAgainHelper(self, nestedList, prevSum):
        totalSum = prevSum
        nextLevel = []
        for x in nestedList:
            if x.isInteger():
                totalSum += x.getInteger()
            else:
                nextLevel.extend(x.getList())
        
        if nextLevel:
            return totalSum + self.depthSumInverseAgainHelper(nextLevel, totalSum)
        return totalSum

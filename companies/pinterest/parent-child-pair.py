# // Suppose we have some input data describing a graph of relationships between parents and children over multiple generations.
# The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

# // For example, in this diagram, 3 is a child of 1 and 2, and 5 is a child of 4:

# // 1   2   4
# //  \ /   / \
# //   3   5   8
# //    \ / \   \
# //     6   7   9
# [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9)]

# // Write a function that takes this data as input and returns two collections:
# one containing all individuals with zero known parents,
# and one containing all individuals with exactly one known parent.
# // Sample output (pseudocode):
# // [
# //   [1, 2, 4],   // Individuals with zero parents
# //   [5, 7, 8, 9] // Individuals with exactly one parent
# // ]

# // Write a function that, for two given individuals in our dataset,
# returns true if and only if they share at least one ancestor.

# // Sample input and output:
# // parentChildPairs, 3, 8 => false
# // parentChildPairs, 5, 8 => true
# // parentChildPairs, 6, 8 => true
import unittest


class Solution:
    def findParent(self, pairs):
        table = self.buildTable(pairs)

        zeroParents = []
        oneParents = []
        for key, value in table.items():
            if len(value) == 0:
                zeroParents.append(key)
            elif len(value) == 1:
                oneParents.append(key)
        return [zeroParents, oneParents]

    def haveCommonAncestor(self, pairs, x, y):
        table = self.buildTable(pairs)
        if x not in table or y not in table:
            return False

        xAncestors = set()
        self.getAllAncestors(x, table, xAncestors)
        return self.myAncestorIn(y, table, xAncestors)

    def getAllAncestors(self, node, table, ancestors):
        if node not in table or not table[node]:
            return

        for parent in table[node]:
            ancestors.add(parent)
            self.getAllAncestors(parent, table, ancestors)

    def myAncestorIn(self, me, table, yourAncestors):
        if me not in table or not table[me]:
            return False

        for parent in table[me]:
            if parent in yourAncestors or self.myAncestorIn(parent, table, yourAncestors):
                return True
        return False

    def furthestAncestor(self, pairs, x):
        table = self.buildTable(pairs)
        if x not in table:
            return -1

        ansWrapper = [0, x]
        self.furthestAncestorUtil(x, table, ansWrapper, 0)
        return ansWrapper[1]

    def furthestAncestorUtil(self, x, table, ansWrapper, step):
        if ansWrapper[0] < step:
            ansWrapper[0] = step
            ansWrapper[1] = x

        for parent in table[x]:
            self.furthestAncestorUtil(parent, table, ansWrapper, step + 1)

    def buildTable(self, pairs):
        # build table, key is node, value are parents of the node
        table = dict()
        for parent, child in pairs:
            if child not in table:
                table[child] = set()
            if parent not in table:
                table[parent] = set()

            table[child].add(parent)
        return table


class SolutionTest(unittest.TestCase):
    def testFindParents(self):
        pairs = [(1, 3), (2, 3), (3, 6), (5, 6),
                 (5, 7), (4, 5), (4, 8), (8, 9)]
        expected = [[1, 2, 4], [5, 7, 8, 9]]
        sol = Solution()
        self.assertEqual(expected, sol.findParent(pairs))

    def testHaveCommonAncestor(self):
        pairs = [(1, 3), (2, 3), (3, 6), (5, 6),
                 (5, 7), (4, 5), (4, 8), (8, 9)]
        expected = [[1, 2, 4], [5, 7, 8, 9]]
        sol = Solution()
        self.assertFalse(sol.haveCommonAncestor(pairs, 3, 8))
        self.assertTrue(sol.haveCommonAncestor(pairs, 6, 9))
    
    def testFurthestAncestor(self):
        pairs = [(1, 3), (2, 3), (3, 6), (5, 6),
                 (5, 7), (4, 5), (4, 8), (8, 9)]
        expected = [[1, 2, 4], [5, 7, 8, 9]]
        sol = Solution()
        self.assertEqual(4, sol.furthestAncestor(pairs, 7))


if __name__ == '__main__':
    unittest.main()

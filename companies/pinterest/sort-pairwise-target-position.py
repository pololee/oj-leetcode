class Solution:
    def position(self, array, target):
        if not array:
            return 1
        
        array.sort()

        i = 0
        j = len(array) - 1

        while i < j:
            curr = array[i] + array[j]
            if curr > target:
                j -= 1
            else:
                i += 1
        
        if array[i] + array[j] > target:
            return 2 * (i + 1) - 1
        elif array[i] + array[j] < target:
            return 2 * (i + 1) + 1
        return 2 * (i+1)

import unittest

class SolutionTest(unittest.TestCase):
    def testPosition(self):
        sol = Solution()
        array = [1, 2, 5, 10, 11]
        print(sol.position(array, 10))
        print(sol.position(array, 9))
        print(sol.position(array, 23))
        print(sol.position(array, 6))

unittest.main()

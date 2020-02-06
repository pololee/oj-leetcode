# Given a list of digits,
# find the smallest number it can form that is larger than or equal to lower_bound

# Examples:
# Input: [8, 1, 7], "0"
# Output: 178

# Input: [8, 1, 7], "200"
# Output: 718

# Input: [3,...,3,1] (100 * 3), "13...34" (99 * 3)
# Output: 313...3

# Notes I asked:
# - lower_bound: positive integer
# - a list of digits: so each value is from  0, 1, ..., 9
# - you have to use all the digits in the list
# - there could be duplicates in the digit list

from typing import *
import unittest


class Solution:
    def find_smallest(self, digits: List[int], lower_bound: int) -> int:
        if lower_bound <= 0:
            return ""

        lower_bound_digits = self.to_digits(lower_bound, len(digits))
        table = self.to_table(digits)

        solution = []
        if self.find_smallest_util(solution, table, lower_bound_digits, 0):
            return self.to_int(solution)
        return ""

    def find_smallest_util(self, solution, table, lower_bound_digits, idx):
        if idx == len(lower_bound_digits):
            return True

        target = lower_bound_digits[idx]
        if idx == 0 and target == 0:
            target = 1

        if table[target] > 0:
            solution.append(target)
            table[target] -= 1

            if self.find_smallest_util(solution, table, lower_bound_digits, idx + 1):
                return True

            solution.pop()
            table[target] += 1

        candidate = target + 1
        while candidate < 10 and table[candidate] <= 0:
            candidate += 1

        if candidate > 9:
            return False

        solution.append(candidate)
        table[candidate] -= 1
        for i in range(10):
            for _ in range(table[i]):
                solution.append(i)
        return True

    def to_digits(self, value, size):
        ans = []
        while value > 0:
            ans.append(value % 10)
            value = value // 10

        curr_size = len(ans)
        for _ in range(curr_size, size):
            ans.append(0)

        return list(reversed(ans))

    def to_int(self, digits):
        ans = 0
        for val in digits:
            ans = ans * 10 + val

        return ans

    def to_table(self, digits):
        table = [0 for _ in range(10)]
        for x in digits:
            table[x] += 1
        return table


class SolutionTest(unittest.TestCase):
    sol = Solution()

    def test_find_smallest(self):
        self.assertEqual(178, self.sol.find_smallest([8, 1, 7], 10))
        self.assertEqual(178, self.sol.find_smallest([8, 1, 7], 123))
        self.assertEqual(178, self.sol.find_smallest([8, 1, 7], 178))
        self.assertEqual(313, self.sol.find_smallest([3, 1, 3], 134))
        self.assertEqual(130, self.sol.find_smallest([0, 1, 3], 105))
        self.assertEqual(301, self.sol.find_smallest([0, 1, 3], 131))
        self.assertEqual(103, self.sol.find_smallest([0, 1, 3], 1))


if __name__ == "__main__":
    unittest.main()

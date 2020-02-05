# Given a list of digits,
# find the smallest number it can form that is larger than or equal to lower_bound

# Examples:
# Input: [8, 1, 7], "0"
# Output: 178

# Input: [8, 1, 7], "200"
# Output: 718

# Input: [3,...,3,1] (100 * 3), "13...34" (99 * 3)
# Output: 313...3

# Notes I assume:
# lower_bound: positive integer, represented as a string
# a list of digits: so each value is from  0, 1, ..., 9
# return value

from typing import *
import bisect
import unittest

# bisect.bisect(arry, x) returns i so that all(val <= x for val in a[0:i]) and all(val > x for val in a[i:])


class Solution:
    def find_smallest(self, digits: List[int], lower_bound: int) -> int:
        if not digits:
            raise Exception("digits cannot be empty")

        if lower_bound <= 0:
            raise Exception("should be positive number")

        if all(val == 0 for val in digits):
            raise Exception("digits cannot be all zeros")

        lower_bound_digits = self.to_digits(lower_bound)

        if len(digits) < len(lower_bound_digits):
            raise Exception("cannot find a number")

        if len(digits) > len(lower_bound_digits):
            self.to_int(sorted(digits))

        solution = []
        self.find_smallest_util(
            solution, sorted(digits), lower_bound_digits, 0
        )
        return self.to_int(solution)

    def find_smallest_util(self, solution, sorted_digits, lower_bound_digits, idx):
        if idx == len(lower_bound_digits):
            return True

        target = lower_bound_digits[idx]
        candidate_idx = bisect.bisect(sorted_digits, target)
        if candidate_idx == 0:  # all digits larger than target
            solution.extend(sorted_digits)
            return True

        if candidate_idx >= len(sorted_digits) and sorted_digits[candidate_idx - 1] < target:
            return False

        if sorted_digits[candidate_idx - 1] == target:
            solution.append(sorted_digits[candidate_idx - 1])
            new_sorted_digits = sorted_digits[:candidate_idx - 1] + sorted_digits[candidate_idx:]
            if self.find_smallest_util(solution, new_sorted_digits, lower_bound_digits, idx + 1):
                return True
            solution.pop()

        if candidate_idx < len(sorted_digits) and sorted_digits[candidate_idx] > target:
            solution.append(sorted_digits[candidate_idx])
            solution.extend(sorted_digits[:candidate_idx])
            solution.extend(sorted_digits[candidate_idx+1:])
            return True

        return False

    def to_digits(self, lower_bound):
        ans = []
        while lower_bound > 0:
            ans.append(lower_bound % 10)
            lower_bound = lower_bound // 10

        return list(reversed(ans))

    def to_int(self, digits):
        ans = 0
        for val in digits:
            ans = ans * 10 + val

        return ans


class SolutionTest(unittest.TestCase):
    sol = Solution()

    def test_find_smallest(self):
        self.assertEqual(178, self.sol.find_smallest([8, 1, 7], 10))
        self.assertEqual(178, self.sol.find_smallest([8, 1, 7], 123))
        self.assertEqual(178, self.sol.find_smallest([8, 1, 7], 178))
        self.assertEqual(313, self.sol.find_smallest([3, 1, 3], 134))
        self.assertEqual(130, self.sol.find_smallest([0, 1, 3], 105))
        self.assertEqual(301, self.sol.find_smallest([0, 1, 3], 131))

if __name__ == "__main__":
    unittest.main()

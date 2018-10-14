import unittest


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # the key here is to modify the original list
        # because the question has such stupid requirement that
        # only allow O(1) space
        # because we are looking for first missing positive integer
        # let's put the value in the place where it should be
        # if value = 1, then it should in nums[value-1], i.e. nums[0]
        if not nums:
            return 1

        N = len(nums)
        for i in range(N):
            while nums[i] > 0 and nums[i] <= N and nums[nums[i] - 1] != nums[i]:
                tmp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = tmp

        for i in range(N):
            if nums[i] != i + 1:
                return i + 1
        return N + 1


class TestSolution(unittest.TestCase):
    sol = Solution()

    def testFirstMissing(self):
        test = [3, 4, -1, 1]
        self.assertEqual(2, self.sol.firstMissingPositive([3, 4, -1, 1]))
        self.assertEqual(1, self.sol.firstMissingPositive([]))
        self.assertEqual(2, self.sol.firstMissingPositive([1]))
        self.assertEqual(4, self.sol.firstMissingPositive([1, 2, 3]))


if __name__ == "__main__":
    unittest.main()

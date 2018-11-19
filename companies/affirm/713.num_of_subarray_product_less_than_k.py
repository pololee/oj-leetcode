import unittest

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        
        ans = 0
        size = len(nums)
        left = 0
        prod = 1
        for right in range(size):
            prod *= nums[right]

            while prod >= k:
                prod //= nums[left]
                left += 1
            
            ans = ans + (right - left + 1)
        return ans

class SolutionTest(unittest.TestCase):
    def testnumSubarrayProductLessThanK(self):
        sol = Solution()
        self.assertEqual(8, sol.numSubarrayProductLessThanK([10, 5, 2, 6], 100))

if __name__ == "__main__":
    unittest.main()

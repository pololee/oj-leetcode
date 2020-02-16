# [719\. Find K-th Smallest Pair Distance](https://leetcode.com/problems/find-k-th-smallest-pair-distance/)

# Difficulty: **Hard**


# Given an integer array, return the k-th smallest **distance** among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.

# **Example 1:**

# ```
# Input:
# nums = [1,3,1]
# k = 1
# Output: 0
# Explanation:
# Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.
# ```

# **Note:**

# 1.  `2 <= len(nums) <= 10000`.
# 2.  `0 <= nums[i] < 1000000`.
# 3.  `1 <= k <= len(nums) * (len(nums) - 1) / 2`.


# Solution
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1

        counter = [0 for _ in range(1000000)]
        size = len(nums)

        for i in range(size):
            for j in range(i+1, size):
                diff = abs(nums[i] - nums[j])
                counter[diff] += 1

        for i in range(len(counter)):
            if counter[i] >= k:
                return i

            k -= counter[i]

        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.smallestDistancePair([1, 3, 1], 1))

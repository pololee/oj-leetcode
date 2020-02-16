# ### [1296\. Divide Array in Sets of K Consecutive Numbers](https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/)

# Difficulty: **Medium**


# Given an array of integers `nums` and a positive integer `k`, find whether it's possible to divide this array into sets of `k` consecutive numbers
# Return `True` if its possibleotherwise return `False`.

# **Example 1:**

# ```
# Input: nums = [1,2,3,3,4,4,5,6], k = 4
# Output: true
# Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
# ```

# **Example 2:**

# ```
# Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
# Output: true
# Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
# ```

# **Example 3:**

# ```
# Input: nums = [3,3,2,2,1,1], k = 3
# Output: true
# ```

# **Example 4:**

# ```
# Input: nums = [1,2,3,4], k = 3
# Output: false
# Explanation: Each array should be divided in subarrays of size 3.
# ```

# **Constraints:**

# *   `1 <= nums.length <= 10^5`
# *   `1 <= nums[i] <= 10^9`
# *   `1 <= k <= nums.length`


# #### Solution

import collections
from typing import *


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) % k != 0:
            return False

        table = collections.Counter(nums)
        for x in range(table.keys()):
            if not table[x] > 0:
                continue

            freq = table[x]
            for i in range(k):
                if table[x+i] < freq:
                    return False
                table[x+i] -= freq

        return True

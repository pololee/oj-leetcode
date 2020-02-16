# ### [659\. Split Array into Consecutive Subsequences](https://leetcode.com/problems/split-array-into-consecutive-subsequences/)

# Difficulty: **Medium**


# Given an array `nums` sorted in ascending order, return `true` if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.

# **Example 1:**

# ```
# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3
# 3, 4, 5

# ```

# **Example 2:**

# ```
# Input: [1,2,3,3,4,4,5,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3, 4, 5
# 3, 4, 5

# ```

# **Example 3:**

# ```
# Input: [1,2,3,4,4,5]
# Output: False
# ```

# **Constraints:**

# *   `1 <= nums.length <= 10000`


# #### Solution

# Language: **Python3**

# ```python3
# class Solution:
#     def isPossible(self, nums: List[int]) -> bool:
#         
# ```

import collections


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        if not nums:
            return False

        freq = collections.Counter(nums)
        need = collections.defaultdict(int)

        for x in nums:
            if freq[x] == 0:
                continue

            if need[x] > 0:
                need[x] -= 1
                need[x+1] += 1
            elif freq[x+1] > 0 and freq[x+2] > 0:
                freq[x+1] -= 1
                freq[x+2] -= 1
                need[x+3] += 1
            else:
                return False

            freq[x] -= 1

        return True

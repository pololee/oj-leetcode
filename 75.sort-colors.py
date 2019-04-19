# ### [75\. Sort Colors](https://leetcode.com/problems/sort-colors/)

# Difficulty: **Medium**


# Given an array with _n_ objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# **Note:** You are not suppose to use the library's sort function for this problem.

# **Example:**

# ```
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]```

# **Follow up:**

# *   A rather straight forward solution is a two-pass algorithm using counting sort.
#     First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
# *   Could you come up with a one-pass algorithm using only constant space?


# #### Solution

# Language: **Python3**

# https://en.wikipedia.org/wiki/Dutch_national_flag_problem

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        redIdx, whiteIdx, blueIdx = 0, 0, len(nums) - 1

        while whiteIdx <= blueIdx:
            if nums[whiteIdx] < 1:
                nums[redIdx], nums[whiteIdx] = nums[whiteIdx], nums[redIdx]
                redIdx += 1
                whiteIdx += 1
            elif nums[whiteIdx] > 1:
                nums[whiteIdx], nums[blueIdx] = nums[blueIdx], nums[whiteIdx]
                blueIdx -= 1
            else:
                whiteIdx += 1

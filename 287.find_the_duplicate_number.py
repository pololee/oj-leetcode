### [287\. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

# Difficulty: **Medium**


# Given an array _nums_ containing _n_ + 1 integers where each integer is between 1 and _n_ (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

# **Example 1:**

# ```
# Input: [1,3,4,2,2]
# Output: 2
# ```

# **Example 2:**

# ```
# Input: [3,1,3,4,2]
# Output: 3```

# **Note:**

# 1.  You **must not** modify the array (assume the array is read only).
# 2.  You must use only constant, _O_(1) extra space.
# 3.  Your runtime complexity should be less than _O_(_n_<sup>2</sup>).
# 4.  There is only one duplicate number in the array, but it could be repeated more than once.


# #### Solution

# Language: **Python3**

# ```python3

# http://yucoding.blogspot.com/2017/01/leetcode-question-find-duplicate-number.html
# It's a fucking brilliant problem'.
# You need to look at every fucking word in the problem.
# There are n + 1 integers
# The value are [1, n], i.e. every value can server a valid index
#
# It doesn'a allow you to use any extra space.
#
# Think about the find circle entry node in linked list
#
# How to construct the linked list
# Every value can serve a valid index
# So the dummy head node would be index 0
# next node's index nums[0]
#
# the last question is how to determine the start point of the linked list.
# We could use the 1st element, since the index of 1st element in array is always 0, 
# and there is no 0 in the value (it starts from 1). So it is impossible that 1st is in the loop.
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return -1
        
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
        
        fast = 0
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow

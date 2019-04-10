# ### [239\. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

# Difficulty: **Hard**


# Given an array _nums_, there is a sliding window of size _k_ which is moving from the very left of the array to the very right. You can only see the _k_ numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

# **Example:**

# ```
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:

# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# ```

# **Note:**
# You may assume _k_ is always valid, 1 ≤ k ≤ input array's size for non-empty array.

# **Follow up:**
# Could you solve it in linear time?


# #### Solution

# Language: **Python3**

# ```python3
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         
# ```
from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        ans, queue = [], deque()
        for i in range(k-1):
            self.inQueue(queue, nums, i)

        for i in range(k-1, len(nums)):
            self.inQueue(queue, nums, i)
            ans.append(nums[queue[0]])
            self.deQueue(queue, nums, i-k+1)

        return ans

    def inQueue(self, queue, nums, idx):
        while queue and nums[queue[-1]] <= nums[idx]:
            queue.pop()
        queue.append(idx)

    def deQueue(self, queue, nums, idx):
        if queue and queue[0] == idx:
            queue.popleft()

# ### [628\. Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers/)

# Difficulty: **Easy**


# Given an integer array, find three numbers whose product is maximum and output the maximum product.

# **Example 1:**

# ```
# Input: [1,2,3]
# Output: 6
# ```

# **Example 2:**

# ```
# Input: [1,2,3,4]
# Output: 24
# ```

# **Note:**

# 1.  The length of the given array will be in range [3,10<sup>4</sup>] and all elements are in the range [-1000, 1000].
# 2.  Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.


# #### Solution

# Language: **Python3**

# ```python3
# class Solution:
#     def maximumProduct(self, nums: List[int]) -> int:
#         
# ```
import heapq


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        return max(
            nums[0] * nums[1] * nums[-1],
            nums[-1] * nums[-2] * nums[-3],
        )

class FastSolution:
    def maximumProduct(self, nums: List[int]) -> int:
        minHeap = [] # two smallest elements
        maxHeap = [] # three largest elements

        for x in nums:
            heapq.heappush(minHeap, -x)
            heapq.heappush(maxHeap, x)

            if len(minHeap) > 2:
                heapq.heappop(minHeap)
            if len(maxHeap) > 3:
                heapq.heappop(maxHeap)
        
        candidates = [maxHeap[0] * maxHeap[1] * maxHeap[2]]
        candidates.append(
            max(maxHeap) * minHeap[0] * (-1) * minHeap[1] * (-1)
        )

        return max(candidates)

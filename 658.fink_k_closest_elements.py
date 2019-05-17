# ### [658\. Find K Closest ElementsCopy for Markdown](https://leetcode.com/problems/find-k-closest-elements/)

# Difficulty: **Medium**


# Given a sorted array, two integers `k` and `x`, find the `k` closest elements to `x` in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

# **Example 1:**

# ```
# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]
# ```

# **Example 2:**

# ```
# Input: [1,2,3,4,5], k=4, x=-1
# Output: [1,2,3,4]
# ```

# **Note:**

# 1.  The value k is positive and will always be smaller than the length of the sorted array.
# 2.  Length of the given array is positive and will not exceed 10<sup>4</sup>
# 3.  Absolute value of elements in the array and x will not exceed 10<sup>4</sup>

# * * *

# **<font color="red" style="display: inline;">UPDATE (2017/9/19):</font>**
# The _arr_ parameter had been changed to an **array of integers** (instead of a list of integers). **_Please reload the code definition to get the latest changes_**.


# #### Solution

# Language: **Python3**

# ```python3
# https://medium.com/@lenchen/leetcode-658-find-k-closest-elements-1755777b9aaf
# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         if not arr:
#             return arr

#         left = 0
#         right = len(arr) - k

#         while left < right:
#             mid = left + (right - left) // 2

#             # mid + k is closer to x, discard mid by assigning left = mid + 1
#             if x - arr[mid] > arr[mid+k] - x:
#                 left = mid + 1
#             # mid is equal or closer to x than mid + k, remains mid as candidate
#             else:
#                 right = mid

#         return arr[left:left+k]


class SolutionII:
    def findClosestElements(self, arr, k, x):
        if not arr:
            return arr
        
        left, right = 0, len(arr) - 1
        while right - left >= k:
            if abs(x - arr[left]) > abs(x - arr[right]):
                left += 1
            else:
                right -= 1
        
        return arr[left:right+1]

if __name__ == "__main__":
    sol = SolutionII()
    arr = [0,0,0,1,3,5,6,7,8,8]
    print(sol.findClosestElements(arr, 2, 2))

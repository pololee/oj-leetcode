# ### [59\. Spiral Matrix IICopy for MarkdownCopy for Markdown](https://leetcode.com/problems/spiral-matrix-ii/)

# Difficulty: **Medium**


# Given a positive integer _n_, generate a square matrix filled with elements from 1 to _n_<sup>2</sup> in spiral order.

# **Example:**

# ```
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]
# ```


# #### Solution

# Language: **Python3**

# ```python3
# class Solution:
#     def generateMatrix(self, n: int) -> List[List[int]]:
#         
# ```
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for _ in range(n)]
                for _ in range(n)]
        
        rowBegin, rowEnd = 0, n - 1
        colBegin, colEnd = 0, n - 1
        direction = 0
        value = 1

        while rowBegin <= rowEnd and colBegin <= colEnd:
            if direction == 0:
                for i in range(colBegin, colEnd + 1):
                    ans[rowBegin][i] = value
                    value += 1
                rowBegin += 1
            elif direction == 1:
                for i in range(rowBegin, rowEnd + 1):
                    ans[i][colEnd] = value
                    value += 1
                colEnd -= 1
            elif direction == 2:
                for i in reversed(range(colBegin, colEnd)):
                    ans[rowEnd][i] = value
                    value += 1
                rowEnd -= 1
            elif direction == 3:
                for i in reversed(range(rowBegin, rowEnd + 1)):
                    ans[i][colBegin] = value
                    value += 1
                colBegin += 1
            direction = (direction + 1) % 4
        
        return ans

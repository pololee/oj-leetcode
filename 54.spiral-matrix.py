# ### [54\. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)

# Difficulty: **Medium**


# Given a matrix of _m_ x _n_ elements (_m_ rows, _n_ columns), return all elements of the matrix in spiral order.

# **Example 1:**

# ```
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# ```

# **Example 2:**

# ```
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# ```


# #### Solution
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        rowBegin, rowEnd = 0, len(matrix) - 1
        colBegin, colEnd = 0, len(matrix[0]) - 1
        ans = []
        direction = 0

        while rowBegin <= rowEnd and colBegin <= colEnd:
            if direction == 0:
                for i in range(colBegin, colEnd + 1):
                    ans.append(matrix[rowBegin][i])
                rowBegin += 1
            elif direction == 1:
                for i in range(rowBegin, rowEnd + 1):
                    ans.append(matrix[i][colEnd])
                colEnd -= 1
            elif direction == 2:
                for i in reversed(range(colBegin, colEnd + 1)):
                    ans.append(matrix[rowEnd][i])
                rowEnd -= 1
            elif direction == 3:
                for i in reversed(range(rowBegin, rowEnd + 1)):
                    ans.append(matrix[i][colBegin])
                colBegin += 1

            direction = (direction + 1) % 4
        return ans

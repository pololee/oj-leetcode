# ### [22\. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

# Difficulty: **Medium**


# Given _n_ pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given _n_ = 3, a solution set is:

# ```
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
# ```


# #### Solution

# Language: **Python3**

# ```python3
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         
# ```

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]

        ans = []
        self.backtrack(ans, [], 0, 0, n)
        return ans

    def backtrack(self, ans, sofar, openCnt, closeCnt, totalCnt):
        if len(sofar) == 2*totalCnt:
            ans.append("".join(sofar))
            return

        if openCnt < totalCnt:
            sofar.append("(")
            self.backtrack(ans, sofar, openCnt + 1, closeCnt, totalCnt)
            sofar.pop()
        if closeCnt < openCnt:
            sofar.append(")")
            self.backtrack(ans, sofar, openCnt, closeCnt + 1, totalCnt)
            sofar.pop()


sol = Solution()
print(sol.generateParenthesis(3))

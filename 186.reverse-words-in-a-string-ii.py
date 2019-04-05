# ### [186\. Reverse Words in a String II](https://leetcode.com/problems/reverse-words-in-a-string-ii/)

# Difficulty: **Medium**


# Given an input string, reverse the string word by word. 

# **Example:**

# ```
# Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]```

# **Note: **

# *   A word is defined as a sequence of non-space characters.
# *   The input string does not contain leading or trailing spaces.
# *   The words are always separated by a single space.

# **Follow up: **Could you do it _in-place_ without allocating extra space?


# #### Solution

# Language: **Python3**

# ```python3

from typing import List


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        if not s:
            return
        
        self.reverse(s, 0, len(s) - 1)
        
        start, end = 0, 0
        while start < len(s):
            while end < len(s) and s[end] != " ":
                end += 1
            
            self.reverse(s, start, end - 1)
            start = end + 1
            end = end + 1

    def reverse(self, chars, start, end):
        while start < end:
            chars[start], chars[end] = chars[end], chars[start]
            start += 1
            end -= 1

sol = Solution()
print(sol.reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))

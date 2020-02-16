# [916\. Word Subsets](https://leetcode.com/problems/word-subsets/)

# Difficulty: **Medium**


# We are given two arrays `A` and `B` of words.  Each word is a string of lowercase letters.

# Now, say that word `b` is a subset of word `a`if every letter in `b` occurs in `a`, **including multiplicity**.  For example, `"wrr"` is a subset of `"warrior"`, but is not a subset of `"world"`.

# Now say a word `a` from `A` is _universal_ if for every `b` in `B`, `b` is a subset of `a`. 

# Return a list of all universal words in `A`.  You can return the words in any order.


# **Example 1:**

# ```
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
# Output: ["facebook","google","leetcode"]
# ```


# **Example 2:**

# ```
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
# Output: ["apple","google","leetcode"]
# ```


# **Example 3:**

# ```
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
# Output: ["facebook","google"]
# ```


# **Example 4:**

# ```
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
# Output: ["google","leetcode"]
# ```


# **Example 5:**

# ```
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
# Output: ["facebook","leetcode"]
# ```

# **Note:**

# 1.  `1 <= A.length, B.length <= 10000`
# 2.  `1 <= A[i].length, B[i].length <= 10`
# 3.  `A[i]` and `B[i]` consist only of lowercase letters.
# 4.  All words in `A[i]` are unique: there isn't `i != j` with `A[i] == A[j]`.


# #### Solution

# Language: **Python3**

from typing import List
from collections import Counter


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        bmax = self.bMax(B)

        ans = []
        for x in A:
            if self.isUniversal(Counter(x), bmax):
                ans.append(x)
        return ans

    def isUniversal(self, candidateCnter, bmax):
        for char, cnt in bmax.items():
            if char not in candidateCnter or candidateCnter[char] < cnt:
                return False

        return True

    def bMax(self, B):
        bmax = dict()
        for x in B:
            xCnter = Counter(x)
            for char, cnt in xCnter.items():
                if char not in bmax or cnt > bmax[char]:
                    bmax[char] = cnt

        return bmax


sol = Solution()
print(sol.wordSubsets(
    ["amazon", "apple", "facebook", "google", "leetcode"],
    ["ec", "oc", "ceo"]
))

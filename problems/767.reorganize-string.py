# ### [767\. Reorganize String](https://leetcode.com/problems/reorganize-string/)

# Difficulty: **Medium**


# Given a string `S`, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

# If possible, output any possible result.  If not possible, return the empty string.

# **Example 1:**

# ```
# Input: S = "aab"
# Output: "aba"
# ```

# **Example 2:**

# ```
# Input: S = "aaab"
# Output: ""
# ```

# **Note:**

# *   `S` will consist of lowercase letters and have length in range `[1, 500]`.


# #### Solution

# Language: **Python3**

import heapq
import collections


class Key:
    def __init__(self, ch, cnt):
        self.ch = ch
        self.cnt = cnt

    def __lt__(self, other):
        return self.cnt > other.cnt

    def __eq__(self, other):
        return self.cnt == other.cnt

    def __gt__(self, other):
        return self.cnt < other.cnt


class Solution:
    def reorganizeString(self, S: str) -> str:
        if not S:
            return ""

        table = collections.Counter(S)
        heap = []
        for ch, cnt in table.items():
            heapq.heappush(heap, Key(ch, cnt))

        ans = []
        prev = None
        while heap:
            key = heapq.heappop(heap)

            ans.append(key.ch)
            if prev:
                heapq.heappush(heap, prev)
                prev = None

            if key.cnt > 1:
                key.cnt -= 1
                prev = key

        if len(ans) == len(S):
            return "".join(ans)
        return ""

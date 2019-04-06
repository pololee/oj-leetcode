# ### [273\. Integer to English Words](https://leetcode.com/problems/integer-to-english-words/)

# Difficulty: **Hard**


# Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2<sup>31</sup> - 1.

# **Example 1:**

# ```
# Input: 123
# Output: "One Hundred Twenty Three"
# ```

# **Example 2:**

# ```
# Input: 12345
# Output: "Twelve Thousand Three Hundred Forty Five"```

# **Example 3:**

# ```
# Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# ```

# **Example 4:**

# ```
# Input: 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
# ```


# #### Solution

# Language: **Python3**

# ```python3

class Solution:
    LESS_THAN_TWENTY = [
        "", "One", "Two", "Three", "Four", "Five",
        "Six", "Seven", "Eight", "Nine", "Ten",
        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
        "Sixteen", "Seventeen", "Eighteen", "Nineteen"
    ]

    TEN_TIMES = [
        "", "", "Twenty", "Thirty", "Forty", "Fifty",
        "Sixty", "Seventy", "Eighty", "Ninety"
    ]

    UNIT = [
        "Thousand", "Million", "Billion"
    ]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        if num % 1000 > 0:
            ans = self.convertHundred(num % 1000)

        for i in range(3):
            num //= 1000

            if num % 1000 > 0:
                curr = self.convertHundred(num % 1000)
                curr.append(self.UNIT[i])
                ans = curr + ans

        return "".join(ans)

    def convertHundred(self, num):
        ans = []

        x, y = num // 100, num % 100

        if x > 0:
            ans.append(self.LESS_THAN_TWENTY[x])
            ans.append('Hundred')

        if y == 0:
            return ans

        if y < 20:
            ans.append(self.LESS_THAN_TWENTY[y])
        else:
            a, b = y // 10, y % 10
            ans.append(self.TEN_TIMES[a])
            if b > 0:
                ans.append(self.LESS_THAN_TWENTY[b])

        return ans

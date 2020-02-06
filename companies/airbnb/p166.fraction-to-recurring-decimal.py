# ### [166\. Fraction to Recurring Decimal](https://leetcode.com/problems/fraction-to-recurring-decimal/)

# Difficulty: **Medium**


# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

# If the fractional part is repeating, enclose the repeating part in parentheses.

# **Example 1:**

# ```
# Input: numerator = 1, denominator = 2
# Output: "0.5"
# ```

# **Example 2:**

# ```
# Input: numerator = 2, denominator = 1
# Output: "2"
# ```

# **Example 3:**

# ```
# Input: numerator = 2, denominator = 3
# Output: "0.(6)"
# ```


# #### Solution

# Language: **Python3**

# ```python3
# class Solution:
#     def fractionToDecimal(self, numerator: int, denominator: int) -> str:
#         if denominator == 0:
#             return ""
#         
#         
#         
# ```
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        if denominator == 0:
            raise Exception("denominator cannot be zero")

        ans = []
        if (numerator < 0) ^ (denominator < 0):
            ans.append('-')

        numerator = abs(numerator)
        denominator = abs(denominator)

        res = numerator // denominator
        ans.append(str(res))
        remainder = numerator % denominator

        if remainder == 0:
            return ''.join(ans)

        ans.append('.')
        table = dict()

        while remainder != 0:
            if remainder in table:
                idx = table[remainder]
                part1 = ''.join(ans[:idx])
                part2 = ''.join(ans[idx:])
                return "{}({})".format(part1, part2)

            table[remainder] = len(ans)
            res = (remainder * 10) // denominator
            ans.append(str(res))
            remainder = (remainder * 10) % denominator

        return ''.join(ans)

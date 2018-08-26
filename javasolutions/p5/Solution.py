class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        size = len(s)
        longest = ''
        for i in range(2 * size):
            left = i // 2
            right = i % 2 + left

            while left >= 0 and right < size:
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break
            substr = s[left + 1:right]
            if len(substr) > len(longest):
                longest = str(substr)
        return longest

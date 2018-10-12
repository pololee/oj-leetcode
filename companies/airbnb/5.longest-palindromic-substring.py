class Solution:
    def longestPalindromicSubstring(self, s):
        if not s:
            return ''
        
        size = len(s)
        longest = ''

        for i in range(2 * size): # 2*size - 1 position to expand
            left = i // 2
            right = i % 2 + left

            while left >= 0 and right < size:
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break
            substr = s[left + 1:right] # exclude left and right
            if len(substr) > len(longest):
                longest = substr
        
        return longest

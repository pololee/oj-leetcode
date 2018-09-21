class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        ans = ''
        for i in range(2 * size - 1):
            left = i // 2
            right = i // 2 + i % 2
            current = self.extend(left, right, s)
            if len(current) > len(ans):
                ans = current
        
        return ans
    
    def extend(self, left, right, s):
        while left >= 0 and s[left] == " ":
            left -= 1
        
        while right < len(s) and s[right] == " ":
            right += 1

        while left >= 0 and right < len(s) and s[left].lower() == s[right].lower():
            left -= 1
            while left >= 0 and s[left] == " ":
                left -= 1
            right += 1
            while right < len(s) and s[right] == " ":
                right += 1
        
        return s[left + 1 : right]

def main():
    sol = Solution()
    print(sol.longestPalindrome("aibohphobia"))
    print(sol.longestPalindrome("nurses run"))
    print(sol.longestPalindrome("Abba"))
    print(sol.longestPalindrome("I went to my gym yesterday")) # " my gym "

if __name__ == '__main__':
    main()


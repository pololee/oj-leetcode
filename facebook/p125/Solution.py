class Solution:
    def is_palindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: return True

        left = 0
        right = len(s) - 1
        s = s.lower()
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while right > left and not s[right].isalnum():
                right -= 1

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

def main():
    sol = Solution()
    test1 = "A man, a plan, a canal: Panama"
    print(sol.is_palindrome(test1)) # expected true
    test2 = "race a car"
    print(sol.is_palindrome(test2)) # expect false
    test3 = '.,'
    print(sol.is_palindrome(test3)) # expect true


if __name__ == '__main__':
    main()

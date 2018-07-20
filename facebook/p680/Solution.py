# If the beginning and end characters of a string are the same (ie. s[0] == s[s.length - 1]), 
# then whether the inner characters are a palindrome (s[1], s[2], ..., s[s.length - 2]) 
# uniquely determines whether the entire string is a palindrome.

class Solution:
    def valid_palindrome(self, s):
        """
        :s type: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.is_palindrome(s, left + 1, right) or self.is_palindrome(s, left, right - 1)
        return True
    
    def is_palindrome(self, s, left, right):
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

if __name__ == '__main__':
    sol = Solution()
    # print(sol.valid_palindrome('abca')) # expect True
    # print(sol.valid_palindrome('abcd')) # expect False
    print(
        sol.valid_palindrome(
            'aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga'
        )) # expect True

class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype list[list[str]]
        """
        answers = []
        self.backtrack([], s, 0, answers)
        return answers

    def backtrack(self, so_far, s, start, answers):
        if start == len(s):
            answers.append(so_far.copy())
        else:
            for i in range(start, len(s)):
                if self.is_palindrome(s, start, i):
                    so_far.append(s[start:i+1])
                    self.backtrack(so_far, s, i + 1, answers)
                    so_far.pop()

    def is_palindrome(self, s, low, high):
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.partition('aab'))
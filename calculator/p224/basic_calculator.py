import unittest


class Solution:
    def evaluate(self, s):
        i = 0
        size = len(s)

        ans = 0
        sign = 1

        while i < size:
            if s[i].isdigit():
                num, i = self.parseNum(s, i)
                ans += (sign * num)
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                left = i
                i = self.parseBrackets(s, left)
                value = self.evaluate(s[left + 1:i])
                ans += (sign * value)
            i += 1

        return ans

    def parseNum(self, s, start):
        num = int(s[start])
        end = start
        size = len(s)
        while end + 1 < size and s[end+1].isdigit():
            num = num * 10 + int(s[end+1])
            end += 1
        return num, end

    def parseBrackets(self, s, left):
        right = left + 1
        size = len(s)
        cnt = 1
        while right < size and cnt > 0:
            if s[right] == '(':
                cnt += 1
            elif s[right] == ')':
                cnt -= 1
            right += 1
        return right - 1

class SolutionTest(unittest.TestCase):
    def testEvaluate(self):
        sol = Solution()
        test = "(1+(4+5+2)-3)+(6+8)"
        self.assertEqual(23, sol.evaluate(test))

if __name__ == "__main__":
    unittest.main()

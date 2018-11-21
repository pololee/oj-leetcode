import unittest

class Solution:
    def postfixToPrefix(self, s):
        if not s:
            return ''
        
        size = len(s)
        stack = []
        for i in range(size):
            ch = s[i]

            if ch in ('+', '-', '*', '/'):
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append("{}{}{}".format(ch, op2, op1))
            else:
                stack.append(ch)
        
        return stack[-1]

class SolutionTest(unittest.TestCase):
    def testPostfixToPrefix(self):
        sol = Solution()
        self.assertEqual("*+AB-CD", sol.postfixToPrefix("AB+CD-*"))
        self.assertEqual("*-A/BC-/AKL", sol.postfixToPrefix("ABC/-AK/L-*"))
        # (A-B/C)*(A/K-L)
        # *-A/BC-/AKL

if __name__ == "__main__":
    unittest.main()

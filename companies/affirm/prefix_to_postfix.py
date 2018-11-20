import unittest

class Solution:
    def prefixToPostfix(self, s):
        if not s:
            return s
        
        size = len(s)
        stack = []
        for i in reversed(range(size)):
            if s[i] in ("+", "-", "*", "/"):
                # because we read from end to start,
                # so the top on stack is the first operand
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append("{}{}{}".format(op1, op2, s[i]))
            else:
                stack.append(s[i])
        return stack[-1]

class SolutionTest(unittest.TestCase):
    def testPrefixToPostfix(self):
        test = "*-A/BC-/AKL"
        sol = Solution()
        self.assertEqual("ABC/-AK/L-*", sol.prefixToPostfix(test))
        self.assertEqual("AB+CD-*", sol.prefixToPostfix("*+AB-CD"))

if __name__ == "__main__":
    unittest.main()

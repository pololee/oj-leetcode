import unittest
from collections import defaultdict

class Solution:
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        # return self.helper(expression, dict())
        return self.helperWithoutCopy(expression, defaultdict(list))

    def helper(self, s, table):
        if s[0] == '-' or s[0].isdigit():
            return int(s)

        if s[0] != '(':
            return table[s]

        # get rid of the leading '(' and tailing ')'
        s = s[1:len(s)-1]
        component, i = self.parse(s, 0)
        if component == "let":
            while True:
                var, i = self.parse(s, i)
                if i >= len(s):
                    return self.helper(var, table.copy())
                valueExpr, i = self.parse(s, i)
                table[var] = self.helper(valueExpr, table.copy())
        elif component == "add":
            first, i = self.parse(s, i)
            second, i = self.parse(s, i)
            return self.helper(first, table.copy()) + self.helper(second, table.copy())
        elif component == "mult":
            first, i = self.parse(s, i)
            second, i = self.parse(s, i)
            return self.helper(first, table.copy()) * self.helper(second, table.copy())
    
    def helperWithoutCopy(self, s, table):
        if s[0] == '-' or s[0].isdigit():
            return int(s)

        if s[0] != '(':
            return table[s][-1]
        
        s = s[1:len(s)-1]
        component, i = self.parse(s, 0)
        if component == "let":
            variables = []
            while True:
                compTmp, i = self.parse(s, i)
                if i >= len(s):
                    # means compTmp is the expr part in let v1 e1 v2 e2 ... vn en expr
                    ans = self.helperWithoutCopy(compTmp, table)
                    for x in variables:
                        table[x].pop()
                    return ans
                variables.append(compTmp)
                valueTmp, i = self.parse(s, i)
                value = self.helperWithoutCopy(valueTmp, table)
                table[compTmp].append(value)
        elif component == "add":
            first, i = self.parse(s, i)
            second, i = self.parse(s, i)
            return self.helperWithoutCopy(first, table) + self.helperWithoutCopy(second, table)
        elif component == "mult":
            first, i = self.parse(s, i)
            second, i = self.parse(s, i)
            return self.helperWithoutCopy(first, table) * self.helperWithoutCopy(second, table)

    def parse(self, s, start):
        end = start + 1
        size = len(s)
        ans = ''

        if s[start] == '(':
            cnt = 1
            while end < size and cnt > 0:
                if s[end] == '(':
                    cnt += 1
                elif s[end] == ')':
                    cnt -= 1
                end += 1
            ans = s[start:end]
            if end < size and s[end] == ' ':
                end += 1
        else:
            while end < size and s[end] != ' ':
                end += 1
            ans = s[start:end]
            if end < size and s[end] == ' ':
                end += 1

        return ans, end


class SolutionTest(unittest.TestCase):
    def testParse(self):
        sol = Solution()
        test = "add "
        component, i = sol.parse(test, 0)
        self.assertEqual("add", component)
        self.assertEqual(4, i)

        test = "((add 1 2))"  # size 11
        component, i = sol.parse(test, 0)
        self.assertEqual(test, component)
        self.assertEqual(11, i)

        test = "(add 1 2) (add 3 4)"
        component, i = sol.parse(test, 0)
        self.assertEqual("(add 1 2)", component)
        self.assertEqual(10, i)
    
    def testEvaluate1(self):
        sol = Solution()
        test = "(add 1 2)"
        self.assertEqual(3, sol.evaluate(test))

    def testEvaluate2(self):
        sol = Solution()
        test = "(mult 3 (add 2 3))"
        self.assertEqual(15, sol.evaluate(test))

    def testEvaluate3(self):
        sol = Solution()
        test = "(let x 2 (mult x 5))"
        self.assertEqual(10, sol.evaluate(test))


if __name__ == "__main__":
    unittest.main()

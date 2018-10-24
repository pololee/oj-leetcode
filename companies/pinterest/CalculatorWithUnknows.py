import unittest

class CalculatorWithUnknowns:
    def evaluate(self, s, knownVars):
        if not s:
            return ''

        ops = []
        nums = []

        size = len(s)
        i = 0
        while i < size:
            ch = s[i]

            if ch == '(':
                ops.append(ch)
            elif ch == ')':
                while ops and ops[-1] != '(':
                    self.perform(ops, nums)
                    if isinstance(nums[-1], str):
                        num = nums.pop()
                        nums.append('({})'.format(num))
                ops.pop() # '('
            elif ch in ('+', '-', '*', '/'):
                while ops and self.shouldPerform(ops[-1], ch):
                    self.perform(ops, nums)
                ops.append(ch)
            elif ch.isdigit():
                num = int(ch)
                while i + 1 < size and s[i+1].isdigit():
                    num = num * 10 + int(s[i+1])
                    i += 1
                nums.append(num)
            elif ch.islower():
                if ch in knownVars:
                    nums.append(knownVars[ch])
                else:
                    nums.append(ch)

            i += 1
        
        while ops:
            self.perform(ops, nums)
        
        return nums[-1]

    def perform(self, ops, nums):
        print(ops)
        print(nums)
        print()
        operator = ops.pop()
        right = nums.pop()
        left = nums.pop()

        if isinstance(right, str) or isinstance(left, str):
            res = "{}{}{}".format(left, operator, right)
            nums.append(res)
        else:
            if operator == '+':
                nums.append(left + right)
            elif operator == '-':
                nums.append(left - right)
            elif operator == '*':
                nums.append(left * right)
            elif operator == '/':
                nums.append(left // right)

    def shouldPerform(self, prev, curr):
        if prev == '(':
            return False
        if prev in ('+', '-') and curr in ('*', '/'):
            return False
        return True

class SolutionTest(unittest.TestCase):
    sol = CalculatorWithUnknowns()

    def testEvaluate(self):
        expression = "2*(5+5*2)/3+(6/2+8)"
        self.assertEqual(21, )
        print(self.sol.evaluate(expression, dict()))

if __name__=='__main__':
    unittest.main()

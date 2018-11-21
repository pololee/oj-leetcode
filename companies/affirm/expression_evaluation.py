import unittest
from functools import reduce


class ExpressionEvaluation:
    def evaluate(self, s):
        if not s:
            return 0
        return self.evaluateUtil(s.split(' '))

    def evaluateUtil(self, array):
        if not array:
            return 0
        size = len(array)
        i = 0
        operator = ''
        nums = []
        while i < size:
            if array[i] == '(':
                left = i
                i = self.rightBracket(array, left)
                numTmp = self.evaluateUtil(array[left+1:i])
                nums.append(numTmp)
            elif array[i] in ('add', 'mul'):
                operator = array[i]
            else:
                nums.append(int(array[i]))
            i += 1
        
        if not nums:
            return 0
        if operator == 'add':
            return sum(nums)
        elif operator == 'mul':
            return reduce((lambda x, y: x * y), nums)
        return nums[-1]

    def rightBracket(self, array, left):
        right = left + 1
        size = len(array)
        cnt = 1
        while right < size and cnt > 0:
            if array[right] == '(':
                cnt += 1
            elif array[right] == ')':
                cnt -= 1
            right += 1
        return right - 1


class ExpressionEvaluationTest(unittest.TestCase):
    def testEvaluate(self):
        s1 = "( )"
        s2 = "( add )"
        s3 = "( mul )"
        s4 = "( add 1 2 ( mul 3 4 5 ) 6 )"
        sol = ExpressionEvaluation()

        self.assertEqual(0, sol.evaluate(s1))
        self.assertEqual(0, sol.evaluate(s2))
        self.assertEqual(0, sol.evaluate(s3))
        self.assertEqual(69, sol.evaluate(s4))

if __name__ == "__main__":
    unittest.main()

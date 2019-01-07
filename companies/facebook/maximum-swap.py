import unittest


class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num:
            return num

        digits = self.numToDigits(num)
        lastIdx = {}
        for idx, d in enumerate(digits):
            lastIdx[d] = idx

        for idx, d in enumerate(digits):
            for x in reversed(range(d + 1, 9 + 1)):
                if x in lastIdx and lastIdx[x] > idx:
                    xIdx = lastIdx[x]
                    digits[idx], digits[xIdx] = digits[xIdx], digits[idx]
                    return self.digitsToNum(digits)
        return num

    def numToDigits(self, num):
        digits = []
        while num > 0:
            digits.append(num % 10)
            num //= 10

        return list(reversed(digits))

    def digitsToNum(self, digits):
        num = 0
        for d in digits:
            num = num * 10 + d
        return num

class SolutionTest(unittest.TestCase):
    def test_maximumSwap(self):
        sol = Solution()
        self.assertEqual(7236, sol.maximumSwap(2736))
        self.assertEqual(9963, sol.maximumSwap(9963))

if __name__ == "__main__":
    unittest.main()

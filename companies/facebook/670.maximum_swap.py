import unittest


class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = self.numToDigits(num)
        lastPos = dict()
        for idx, value in enumerate(digits):
            lastPos[value] = idx

        for idx, value in enumerate(digits):
            for d in reversed(range(value + 1, 9+1)):
                if d in lastPos and lastPos[d] > idx:
                    lastIdx = lastPos[d]
                    digits[idx], digits[lastIdx] = digits[lastIdx], digits[idx]
                    return self.digitsToNum(digits)
        return num

    def numToDigits(self, num):
        return [int(x) for x in str(num)]

    def digitsToNum(self, digits):
        return int(''.join(map(str, digits)))


class SolutionTest(unittest.TestCase):
    def test_numToDigits(self):
        sol = Solution()
        self.assertListEqual([2, 7, 3, 6], sol.numToDigits(2736))

    def test_digitsToNum(self):
        sol = Solution()
        self.assertEqual(2736, sol.digitsToNum([2, 7, 3, 6]))
    
    def test_maximumSwap(self):
        sol = Solution()
        self.assertEqual(7236, sol.maximumSwap(2736))
        self.assertEqual(98863, sol.maximumSwap(98368))


if __name__ == "__main__":
    unittest.main()

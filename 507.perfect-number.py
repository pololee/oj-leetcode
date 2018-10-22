import math


class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        bound = math.floor(math.sqrt(num))
        divisorsSum = 0

        for x in range(1, bound + 1):
            if num % x == 0:
                divisorsSum += x

                if x * x != num:
                    divisorsSum += (num // x)
        return divisorsSum - num == num # because x == 1 was added, num // 1 = num, so the divisorsSum has num

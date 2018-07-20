class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        DP = [0 for _ in range(num + 1)]
        
        base = 1
        next_base = base * 2
        for i in range(1, num + 1):
            DP[i] = 1 + DP[i - base]

            if base - 1 == i:
                base *= 2
                next_base = base * 2
        

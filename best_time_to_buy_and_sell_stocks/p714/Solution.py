class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # T[i][0] = max(T[i-1][0], T[i-1][1] + prices[i] - fee)
        # T[i][1] = max(T[i-1][1], T[i-1][0] - prices[i])

        if not prices:
            return 0
        
        T_i0 = 0
        T_i1 = -(max(prices) + 1)
        for price in prices:
            T_last0 = T_i0
            T_i0 = max(T_i0, T_i1 + price - fee)
            T_i1 = max(T_i1, T_last0 - price)
        return T_i0

def main():
    sol = Solution()
    print(sol.maxProfit([1, 3, 2, 8, 4, 9], 2))

if __name__ == '__main__':
    main()

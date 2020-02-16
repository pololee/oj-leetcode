class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        # T[-1][2][0] = 0
        # T[-1][2][1] = negative infinity
        # T[i][2][0] = max(T[i-1][2][0], T[i-1][2][1] + prices[i])
        #                  rest, sell
        # T[i][2][1] = max(T[i-1][2][1], T[i-1][1][0] - prices[i])
        #                  rest, buy
        # T[-1][1][0] = 0
        # T[-1][1][1] = negative infinity
        # T[i][1][0] = max(T[i-1][1][0], T[i-1][1][1] + prices[i])
        #                  rest, sell
        # T[i][1][1] = max(T[i-1][1][1], T[i-1][0][0] - prices[i])
        #            = max(T[i-1][1][1], - prices[i])
        #                  rest, buy

        T_i20 = 0
        T_i21 = -(max(prices) + 1)
        T_i10 = 0
        T_i11 = -(max(prices) + 1)
        for price in prices:
            T_i20 = max(T_i20, T_i21 + price)
            T_i21 = max(T_i21, T_i10 - price)
            T_i10 = max(T_i10, T_i11 + price)
            T_i11 = max(T_i11, 0 - price)
            # T_last10 = T_i10
            # T_last20 = T_i20
            # T_last21 = T_i21
            # T_last11 = T_i11

        
            
            # T_i10 = max(T_last10, T_last11 + price)
            # T_i11 = max(T_last11, 0 - price)
            # T_i21 = max(T_last21, T_last10 - price)
            # T_i20 = max(T_last20, T_last21 + price)

        return T_i20


def main():
    sol = Solution()
    print(sol.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
    print(sol.maxProfit([1, 2, 3, 4, 5]))
    print(sol.maxProfit([6, 1, 3, 2, 4, 7])) # expected 7


if __name__ == '__main__':
    main()

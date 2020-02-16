class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
# T[-1][1][0] = 0
# T[-1][1][1] = negative infinity
# T[-1][2][0] = 0
# T[-1][2][1] = negative infinity
# T[i][1][0] = max(T[i-1][1][0], T[i-1][1][1] + prices[i])
# T[i][1][1] = max(T[i-1][1][1], T[i-1][0][0] - prices[i])
# T[i][2][0] = max(T[i-1][2][0], T[i-1][2][1] + prices[i])
# T[i][2][1] = max(T[i-1][2][1], T[i-1][1][0] - prices[i])
# ...
# T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
# T[i][k][1] = max(T[i-1][k][1], T[i-1][k-1][0] - prices[i])
        if not prices or k == 0:
            return 0

        size = len(prices)
        minimum_value = -(max(prices) + 1)
        # the maximum number of profitable transactions is size // 2
        # (you need to buy, sell and you can only keep one stock in your hand)
        # so if k >= size // 2, then we can think it as no limit on transaction number
        if k >= (size // 2):
            T_i0 = 0
            T_i1 = minimum_value
            for price in prices:
                T_last0 = T_i0
                T_i0 = max(T_i0, T_i1 + price)
                T_i1 = max(T_i1, T_last0 - price)
            
            return T_i0
        
        T_ik0 = [0 for _ in range(k + 1)]
        T_ik1 = [minimum_value for _ in range(k + 1)]
        for price in prices:
            for k_idx in reversed(range(1, k + 1)):
                T_ik0[k_idx] = max(T_ik0[k_idx], T_ik1[k_idx] + price)
                T_ik1[k_idx] = max(T_ik1[k_idx], T_ik0[k_idx - 1] - price)
        
        return T_ik0[k]

def main():
    sol = Solution()
    print(sol.maxProfit(2, [2, 4, 1]))
    print(sol.maxProfit(2, [3, 2, 6, 5, 0, 3]))

if __name__ == '__main__':
    main()

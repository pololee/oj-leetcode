class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # T[i][0] = max(T[i-1][0], T[i-1][1] + prices[i])
        # T[i][1] = max(T[i-1][1], T[i-2][0] - prices[i])
        if not prices:
            return 0

        T_ik0_pre = 0
        T_ik0 = 0
        T_ik1 = -(max(prices) + 1)
        for price in prices:
            T_lastk0 = T_ik0
            T_ik0 = max(T_lastk0, T_ik1 + price)
            T_ik1 = max(T_ik1, T_ik0_pre - price)
            T_ik0_pre = T_lastk0
        
        return T_ik0

def main():
    sol = Solution()
    print(sol.maxProfit([1, 2, 3, 0, 2]))

if __name__ == '__main__':
    main()

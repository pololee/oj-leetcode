class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += (prices[i] - prices[i-1])
        return max_profit

class GenericSolution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        T_i0 = 0
        T_i1 = None

        # T[i][0] = max(T[i-1][0], T[i-1][1] + prices[i]) # rest or sell
        # T[i][1] = max(T[i-1][1], T[i-1][1] - prices[i], T[i-1][0] - prices[i])
        #               rest, buy, buy
        #         = max(T[i-1][1], T[i-1][0] - prices[i])
        for price in prices:
            T_last_1 = T_i1
            T_last_0 = T_i0

            if T_last_1:
                T_i0 = max(T_last_0, T_last_1 + price)
            else:
                T_i0 = T_last_0
            
            if T_last_1:
                T_i1 = max(T_last_1, T_last_0 - price)
            else:
                T_i1 = T_last_0 - price
        return T_i0

def main():
    sol = Solution()
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
    gsol = GenericSolution()
    print(gsol.maxProfit([7, 1, 5, 3, 6, 4]))

if __name__ == '__main__':
    main()

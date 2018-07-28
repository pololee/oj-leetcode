# exceed time limit
# class Solution:
#     def max_profit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if not prices: return 0

#         answer = 0
#         for i in range(0, len(prices)):
#             for j in range(i+1, len(prices)):
#                 if prices[j] > prices[i]:
#                     answer = max(answer, prices[j] - prices[i])
#         return answer

class Solution:
    def max_profit(self, prices):
        if not prices: return 0

        min_price_so_far = None
        max_profit_so_far = 0
        for i in range(len(prices)):
            if min_price_so_far is None or min_price_so_far > prices[i]:
                min_price_so_far = prices[i]
            else:
                max_profit_so_far = max(max_profit_so_far, prices[i] - min_price_so_far)
        return max_profit_so_far

class KadaneSolution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        max_current = 0
        max_so_far = 0
        for i in range(1, len(prices)):
            if max_current + prices[i] - prices[i-1] > 0:
                max_current += (prices[i] - prices[i-1])
            else:
                max_current = 0
            
            max_so_far = max(max_so_far, max_current)
        return max_so_far


def main():
    sol = Solution()

    test1 = [7, 1, 5, 3, 6, 4] # answer 5
    test2 = [7, 6, 4, 3, 1] # answer 0
    print(sol.max_profit(test1))
    print(sol.max_profit(test2))

    kadane = KadaneSolution()
    print(kadane.maxProfit(test1))
    print(kadane.maxProfit(test2))

if __name__ == '__main__':
    main()

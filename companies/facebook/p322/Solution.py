class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # DP[i] represent given amount of i, the optimal number of coins needed
        maximum = amount + 1
        DP = [maximum for _ in range(amount + 1)] # DP[amount] is the answer
        DP[0]= 0

        for i in range(1, amount + 1):
            for coin_amt in coins:
                if i - coin_amt >= 0:
                    DP[i] = min(DP[i], DP[i-coin_amt] + 1)
        
        if DP[amount] > amount:
            return -1
        return DP[amount]

def main():
    sol = Solution()
    print(sol.coinChange([1, 2, 5], 11))
    print(sol.coinChange([2], 3))

if __name__ == '__main__':
    main()

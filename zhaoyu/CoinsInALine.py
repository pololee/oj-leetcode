class CoinsInALine:
    def win_or_not(self, n):
        """
        :type n: int
        :rtype boolean
        """
        DP = [None for _ in range(n + 1)]  # 0,...,n coins left => n + 1 cases
        return self.memory_search(n, DP)
    # DP[i]
    # whether I'll win or lose given i coins left and it's my turn to pick
    # 0: empty => I don't know
    # 1: lose => false
    # 2: win => true

    def memory_search(self, n, dp):
        if dp[n]:
            return dp[n]

        if n <= 0:
            dp[n] = False
        elif n == 1 or n == 2:
            dp[n] = True
        elif n == 3:
            dp[n] = False
        else:
#        n                             n
#        +                             +
#        |                             |
#        |                             |
#        v                             v
#       n - 1                         n - 2
#       +   +                         +   +
#       |   |                         |   |
#   <---+   +--->                 <---+   +--->
# n - 2        n - 3           n - 3         n - 4
            # if (self.memeory_search(n-2, dp) and self.memory_search(n -3, dp)) or 
            #    (self.memory_search(n-3, dp) and self.memory_search(n - 4, dp))
            if not self.memory_search(n - 1, dp) or not self.memory_search(n - 2, dp):
                dp[n] = True
            else:
                dp[n] = False

        return dp[n]

def main():
    sol = CoinsInALine()
    print(sol.win_or_not(100)) # True

if __name__ == '__main__':
    main()

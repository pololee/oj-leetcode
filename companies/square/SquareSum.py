class SquareSum:
    def square_sum(self, n):
        """
        :n type: int
        :rtype int
        """
        if n == 0:
            return 0
        if n < 0:
            return self.square_sum(-n)
        
        DP = [0 for _ in range(n+1)]
        DP[1] = 1
        for i in range(2, n + 1):
            DP[i] = DP[i-1] + i + i - 1
        
        return sum(DP)

def main():
    square = SquareSum()
    print(square.square_sum(5))

if __name__ == '__main__':
    main()

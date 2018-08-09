class Backpack2:
    def numberOfCombinations(self, nums, M):
        col_size = M + 1
        row_size = len(nums) + 1

        DP = [[0 for _ in range(col_size)]
              for _ in range(row_size)]
        
        for x in range(row_size):
            DP[x][0] = 1
        
        for y in range(1, col_size):
            DP[0][y] = 0
        
        for i in range(1, row_size):
            for j in range(1, col_size):
                k = 0
                while k * nums[i-1] <= j:
                    DP[i][j] += DP[i-1][j - k * nums[i-1]]
                    k += 1
        
        return DP[row_size-1][col_size-1]

def main():
    sol = Backpack2()
    print(sol.numberOfCombinations([1, 2, 5], 5))
    print(sol.numberOfCombinations([2], 3))
    print(sol.numberOfCombinations([10], 10))

if __name__ == '__main__':
    main()

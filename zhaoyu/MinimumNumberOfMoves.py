class MinimumNumberOfMoves:
    def minMoves(self, nums):
        """
        :type nums: list[int]
        :rtype int
        """
        # a = nums
        # b = sorted(nums)
        # DP[i][j] represents the minimum number of moves
        # to make a[0:i+1] to becomes non-decreasing
        # and each number of a[0:i+1] is at most b[j]
        #
        # DP[0][0] = abs(a[0] - b[0])
        # DP[0][j] = min(DP[0][j-1], abs(a[0] - b[j]))
        # DP[i][0] = DP[i-1][0] + abs(a[i] - b[0])
        # DP[i][j] = min(DP[i][j-1], DP[i-1][j] + abs(a[i] - b[j]))
        increase = self.min_moves_non_descreasing(nums)
        decrease = self.min_moves_non_descreasing(nums[::-1])

        return min(increase, decrease)

    def min_moves_non_descreasing(self, nums):
        a = nums
        b = sorted(nums)

        size = len(nums)
        DP = [[0 for _ in range(size)]
              for _ in range(size)]

        DP[0][0] = abs(a[0] - b[0])

        for i in range(1, size):
            DP[i][0] = DP[i-1][0] + abs(a[i] - b[0])

        for j in range(1, size):
            DP[0][j] = min(DP[0][j-1], abs(a[0] - b[j]))

        for i in range(1, size):
            for j in range(1, size):
                DP[i][j] = min(DP[i][j-1], DP[i-1][j] + abs(a[i] - b[j]))

        return DP[size - 1][size - 1]

def main():
    moves = MinimumNumberOfMoves()
    print(moves.minMoves([1, 1, 5, 2, 2])) # 3 => 1, 1, 2, 2, 2

if __name__ == '__main__':
    main()

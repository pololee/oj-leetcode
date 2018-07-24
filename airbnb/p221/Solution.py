class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # DP[i, j] represents the square area with (i, j) as the lower-right corner
        # DP[i, j] = min(DP[i-1, j-1], DP[i, j - 1], DP[i-1, j]) + 1

        if not matrix or not matrix[0]:
            return 0

        num_of_rows = len(matrix)
        num_of_cols = len(matrix[0])
        side_length_DP = [[0 for _ in range(num_of_cols + 1)]
                  for _ in range(num_of_rows + 1)]
        max_side_length = 0

        for i in range(1, num_of_rows + 1):
            for j in range(1, num_of_cols + 1):
                if matrix[i-1][j-1] == '0':
                    continue
                side_length_DP[i][j] = min(
                    side_length_DP[i-1][j-1], min(side_length_DP[i][j-1], side_length_DP[i-1][j])) + matrix[i-1][j-1]
                max_side_length = max(max_side_length, side_length_DP[i][j])
        return max_side_length * max_side_length

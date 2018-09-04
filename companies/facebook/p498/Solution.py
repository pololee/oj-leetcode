class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        m = len(matrix)
        n = len(matrix[0])
        answer = []

        for xysum in range(m-1+n-1+1):
            if xysum % 2 == 0:  # up
                x = xysum if xysum < m else m - 1
                y = xysum - x

                while x >= 0 and y < n:
                    answer.append(matrix[x][y])
                    x -= 1
                    y += 1
            else:  # down
                y = xysum if xysum < n else n - 1
                x = xysum - y

                while x < m and y >= 0:
                    answer.append(matrix[x][y])
                    x += 1
                    y -= 1
        return answer

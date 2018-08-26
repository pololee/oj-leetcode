from IPython import embed


class Solution:
    DEAD_TO_DEAD = 0
    LIVE_TO_LIVE = 1
    LIVE_TO_DEAD = 2
    DEAD_TO_LIVE = 3

    DIRECTIONS = [(1, 0), (1, 1), (0, 1), (-1, 1),
                  (-1, 0), (-1, -1), (0, -1), (1, -1)]

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                count_lives = 0

                for dx, dy in self.DIRECTIONS:
                    x = i + dx
                    y = j + dy
                    if x < 0 or x >= m or y < 0 or y >= n:
                        continue
                    if board[x][y] == 1 or board[x][y] == 2:
                        count_lives += 1

                if board[i][j] == 1:
                    if count_lives < 2:
                        board[i][j] = self.LIVE_TO_DEAD
                    elif count_lives == 2 or count_lives == 3:
                        board[i][j] = self.LIVE_TO_LIVE
                    else:
                        board[i][j] = self.LIVE_TO_DEAD
                elif board[i][j] == 0:
                    if count_lives == 3:
                        board[i][j] = self.DEAD_TO_LIVE
                    else:
                        board[i][j] = self.DEAD_TO_DEAD

        for i in range(m):
            for j in range(n):
                board[i][j] = board[i][j] % 2


def main():
    board = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]

    sol = Solution()
    sol.gameOfLife(board)
    print(board)


if __name__ == '__main__':
    main()

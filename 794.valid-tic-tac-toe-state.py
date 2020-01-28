import unittest


class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        # The first player always places "X" characters,
        # while the second player always places "O" characters.
        size = len(board)
        xCnt = 0
        oCnt = 0
        
        for i in range(size):
            for j in range(size):
                if board[i][j] == 'X':
                    xCnt += 1
                elif board[i][j] == 'O':
                    oCnt += 1
        
        if xCnt < oCnt or xCnt > oCnt + 1:
            return False
        
        if self.checkWin(board, 'O'):
            if self.checkWin(board, 'X'):
                return False
            return xCnt == oCnt
        
        if self.checkWin(board, 'X') and xCnt != oCnt + 1:
            return False
        
        return True

    def checkWin(self, board, player):
        size = len(board)
        rows = [0 for _ in range(size)]
        cols = [0 for _ in range(size)]
        diag = 0
        antiDiag = 0
        
        for i in range(size):
            for j in range(size):
                if board[i][j] == player:
                    rows[i] += 1
                    cols[j] += 1
                    if i == j:
                        diag += 1
                    
                    if i + j == size - 1:
                        antiDiag += 1
        
        if diag == size or antiDiag == size:
            return True
        
        for i in range(size):
            if rows[i] == size or cols[i] == size:
                return True
        
        return False


class SolutionTest(unittest.TestCase):
    def testValid(self):
        test = ["XXO","XOX","OXO"]
        sol = Solution()
        self.assertFalse(sol.validTicTacToe(test))


if __name__ == "__main__":
    unittest.main()

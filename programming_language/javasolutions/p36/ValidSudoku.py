class ValidSudoku:
    def isValid(self, board):
        if not board or len(board) != 9 or len(board[0]) != 9:
            return False

        # check row
        for i in range(9):
            seen = set()
            for j in range(9):
                if not self.cellValid(board[i][j], seen):
                    return False

        # check col
        for col in range(9):
            seen = set()
            for row in range(9):
                if not self.cellValid(board[row][col], seen):
                    return False

        # check 3x3 grid
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for k in range(9):
                    row = i + k // 3
                    col = i + k % 3
                    if not self.cellValid(board[row][col], seen):
                        return False
        return True

    def cellValid(self, ch, seen):
        if ch == ".":
            return True

        digit = int(ch)
        if digit < 1 or digit > 9 or digit in seen:
            return False

        seen.add(digit)
        return True

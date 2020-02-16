package javasolutions.p37;

public class AnotherSudokuSolver {
  public void solveSudoku(char[][] board) {
    if (board == null || board.length != 9 || board[0].length != 9) {
      return;
    }

    solveSudoKuDFS(board);
  }

  private boolean solveSudoKuDFS(char[][] board) {
    for (int i = 0; i < board.length; i++) {
      for (int j = 0; j < board[0].length; j++) {
        if (board[i][j] == '.') {
          for (char num = '1'; num <= '9'; num++ ) {
            if (isValidSudoku(board, i, j, num)) {
              board[i][j] = num;

              if (solveSudoKuDFS(board)) {
                return true;
              } else {
                board[i][j] = '.';
              }
            }
          }

          return false;
        }
      }
    }

    return true;
  }

  private boolean isValidSudoku(char[][] board, int row, int col, char value) {
    if (row >= 9 || col >= 9) {
      return false;
    }

    // check the row-th row
    for (int i=0; i<9; i++) {
      if (col != i && board[row][i] == value) {
        return false;
      }
    }

    // check the col-th column
    for (int i=0; i<9; i++) {
      if (row != i && board[i][col] == value) {
        return false;
      }
    }

    // check the box
    int beginngRowOfBox = row / 3 * 3;
    int endRowOfBoxPlusOne = row / 3 * 3 + 3;

    int beginningColOfBox = col / 3 * 3;
    int endColOfBoxPlusOne = col / 3 * 3 + 3;

    for (int i=0; i<endRowOfBoxPlusOne; i++) {
      for (int j=0; j<endColOfBoxPlusOne; j++) {
        if ( (row != i || col != j) && board[i][j] == value ) {
          return false;
        }
      }
    }

    return true;
  }
}
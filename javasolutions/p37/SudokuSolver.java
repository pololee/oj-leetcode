package javasolutions.p37;

public class SudokuSolver {
  public void solveSudoku(char[][] board) {
    if (board == null || board.length != 9 || board[0].length != 9) {
      return;
    }

    solveSudokuDFS(board, 0, 0);
  }

  private boolean solveSudokuDFS(char[][] board, int row, int col) {
    if (row >= 9) {
      return true;
    }

    if (col >= 9) {
      return solveSudokuDFS(board, row+1, 0);
    }

    if (board[row][col] != '.') {
      return solveSudokuDFS(board, row, col+1);
    } else {
      for (int num = 1; num <= 9; num++) {

        char value = (char)(num + '0');

        if (isValidSudoku(board, row, col, value)) {
          board[row][col] = value;

          if(solveSudokuDFS(board, row, col+1)) return true;

          board[row][col] = '.';
        }
      }
    }

    return false;
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
package javasolutions.p36;

public class ValidSudoku {
  public boolean isValidSudoKu(char[][] board) {
    if (board == null || board.length != 9 || board[0].length != 9) {
      return false;
    }

    boolean[][] rowFlag = new boolean[9][9];
    boolean[][] colFlag = new boolean[9][9];
    boolean[][] boxFlag = new boolean[9][9];

    for (int row=0; row < 9; row++) {
      for (int col=0; col < 9; col++) {
        if (board[row][col] != '.') {
          int indexOfNum = board[row][col] - '0' - 1; // actual number is board[row][col] - '0'
          int indexOfBox = (row / 3) * 3 + col / 3; // see that attached spreadsheet in the folder

          if (rowFlag[row][indexOfNum] || colFlag[col][indexOfNum] || boxFlag[indexOfBox][indexOfNum]) {
            return false;
          } else {
            rowFlag[row][indexOfNum] = colFlag[col][indexOfNum] = boxFlag[indexOfBox][indexOfNum] = true;
          }
        }
      }
    }

    return true;
  }
}
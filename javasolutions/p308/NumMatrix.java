package javasolutions.p308;

public class NumMatrix {
  private int numOfInputRows;
  private int numOfInputCols;
  private int[][] matrix;
  private int[][] twoDimBIT;

  public NumMatrix(int[][] inputMatrix) {
    if(inputMatrix.length == 0 || inputMatrix[0].length == 0) return;

    numOfInputRows = inputMatrix.length;
    numOfInputCols = inputMatrix[0].length;
    matrix = new int[numOfInputRows][numOfInputCols];
    twoDimBIT = new int[numOfInputRows+1][numOfInputCols+1];

    for (int i=0; i<numOfInputRows; i++) {
      for (int j=0; j<numOfInputCols; j++) {
        update(i, j, inputMatrix[i][j]);
      }
    }
  }

  public void update(int row, int col, int value) {
    if(isInvalidIndex(row, col)) return;

    int delta = value - matrix[row][col];
    matrix[row][col] = value;

    row++;
    col++;

    while(row <= numOfInputRows) {
      int j = col;

      while(j <= numOfInputCols) {
        twoDimBIT[row][j] += delta;
        j += lastSetBit(j);
      }

      row += lastSetBit(row);
    }
  }

  public int getSum(int row, int col) {
    if(isInvalidIndex(row, col)) return 0;

    int sum = 0;
    row++;
    col++;

    while(row > 0) {
      int j = col;

      while(j > 0) {
        sum += twoDimBIT[row][j];
        j -= lastSetBit(j);
      }

      row -= lastSetBit(row);
    }

    return sum;
  }

  public int sumRegion(int row1, int col1, int row2, int col2) {
    return getSum(row2, col2) - getSum(row1-1, col2) - getSum(row2, col1-1) + getSum(row1-1, col1-1);
  }

  public void printTwoDimBIT() {
    for (int i=0; i<=numOfInputRows; i++) {
      for (int j=0; j<=numOfInputCols; j++) {
        System.out.format("%d,", twoDimBIT[i][j]);
      }

      System.out.println();
    }
  }

  private boolean isInvalidIndex(int row, int col) {
    return row < 0 || row >= numOfInputRows || col < 0 || col > numOfInputCols;
  }

  private int lastSetBit(int x) {
    return x & (-x);
  }

  public static void main(String[] args) {
    int[][] test = {
      {1, 2, 3},
      {4, 5, 6},
      {7, 8, 9}
    };

    NumMatrix cal = new NumMatrix(test);
    cal.printTwoDimBIT();

    System.out.println(cal.getSum(1, 2));
    System.out.println(cal.sumRegion(1, 1, 2, 2));
  }
}
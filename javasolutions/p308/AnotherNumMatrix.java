package javasolutions.p308;

public class AnotherNumMatrix {
  public AnotherNumMatrix(int[][] matrix) {
    if(matrix.length == 0 || matrix[0].length == 0) return;

    inputMatrix = matrix;
    numOfInputRows = matrix.length;
    numOfInputCols = matrix[0].length;

    rowSum = new int[numOfInputRows][numOfInputCols+1];

    for (int i=0; i<numOfInputRows; i++) {
      for (int j=1; j<numOfInputCols+1; j++) {
        rowSum[i][j] = rowSum[i][j-1] + inputMatrix[i][j-1];
      }
    }
  }

  public void update(int row, int col, int value) {
    if(invalidIndex(row, col)) return;

    int delta = value - inputMatrix[row][col];
    inputMatrix[row][col] = value;

    for (int j=col+1; j < numOfInputCols+1; j++) {
      rowSum[row][j] += delta;
    }
  }

  public int sumRegion(int row1, int col1, int row2, int col2) {
    if(invalidIndex(row1, col1) || invalidIndex(row2, col2)) return 0;

    int answer = 0;
    for (int i=row1; i<=row2; i++) {
      answer += (rowSum[i][col2+1] - rowSum[i][col1]);
    }

    return answer;
  }

  private boolean invalidIndex(int row, int col) {
    return row < 0 || row >= numOfInputRows || col < 0 || col >= numOfInputCols;
  }

  public void printRowSum() {
    for (int i=0; i<numOfInputRows; i++) {
      for (int j=0; j<numOfInputCols+1; j++) {
        System.out.format("%d, ", rowSum[i][j]);
      }

      System.out.println();
    }
  }

  private int[][] inputMatrix;
  private int[][] rowSum;
  private int numOfInputRows;
  private int numOfInputCols;

  public static void main(String[] args) {
    int[][] test = {
      {1, 1, 1, 1},
      {1, 1, 1, 1},
      {1, 1, 1, 1}
    };

    AnotherNumMatrix cal = new AnotherNumMatrix(test);
    cal.printRowSum();
    System.out.println(cal.sumRegion(0, 1, 1, 3));
    cal.update(0, 1, 2);
    System.out.println(cal.sumRegion(0, 1, 1, 3));
  }
}
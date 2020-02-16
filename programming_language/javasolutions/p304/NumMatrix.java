package javasolutions.p304;

public class NumMatrix {
  private int[][] sumDPMatrix;

  public NumMatrix(int[][] matrix) {
    if(matrix.length == 0 || matrix[0].length == 0) {
      return;
    }

    sumDPMatrix = new int[matrix.length + 1][matrix[0].length + 1];

    for (int i=1; i<=matrix.length; i++) {
      for (int j=1; j<=matrix[0].length; j++) {
        sumDPMatrix[i][j] = sumDPMatrix[i][j-1] + sumDPMatrix[i-1][j] - sumDPMatrix[i-1][j-1] + matrix[i-1][j-1];
      }
    }
  }

  public int sumRegion(int row1, int col1, int row2, int col2) {
    if (sumDPMatrix.length == 0 || sumDPMatrix[0].length == 0) {
      return 0;
    }
    return sumDPMatrix[row2+1][col2+1] - sumDPMatrix[row1][col2+1] - sumDPMatrix[row2+1][col1] + sumDPMatrix[row1][col1];
  }
}
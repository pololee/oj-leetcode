package javasolutions.p59;

public class SpiralMatrixII {
  public int[][] generateMatrix(int n) {
    int[][] matrix = new int[n][n];
    if(n == 0) return matrix;

    int row = 0, col = -1, value = 0;
    int numOfRows = n, numOfCols = n;

    while(true) {
      for (int i=0; i<numOfCols; i++) {
        value++;
        System.out.println(value);
        col++;
        matrix[row][col] = value;
      }

      numOfRows--;
      if(numOfRows == 0) break;

      for (int i=0; i<numOfRows; i++) {
        value++;
        System.out.println(value);
        row++;
        matrix[row][col] = value;
      }

      numOfCols--;
      if(numOfCols == 0) break;

      for (int i=0; i<numOfCols; i++) {
        value++;
        System.out.println(value);
        col--;
        matrix[row][col] = value;
      }

      numOfRows--;
      if(numOfRows == 0) break;

      for (int i=0; i<numOfRows; i++) {
        value++;
        System.out.println(value);
        row--;
        matrix[row][col] = value;
      }

      numOfCols--;
      if(numOfCols == 0) break;
    }

    return matrix;
  }

  public static void main(String[] args) {
    SpiralMatrixII m = new SpiralMatrixII();
    m.generateMatrix(0);
  }
}
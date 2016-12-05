package javasolutions.p54;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class SpiralMatrix {
  public List<Integer> spiralOrder(int[][] matrix) {
    List<Integer> elements = new ArrayList<>();

    if (matrix.length == 0) return elements;

    int numOfRows = matrix.length;
    int numOfColumns = matrix[0].length;

    int row = 0, col = -1;

    while(true) {
      for(int i = 0; i < numOfColumns; i++) {
        col++;
        elements.add(matrix[row][col]);
      }

      numOfRows--;
      if(numOfRows == 0) break;

      for(int i = 0; i < numOfRows; i++) {
        row++;
        elements.add(matrix[row][col]);
      }

      numOfColumns--;
      if(numOfColumns == 0) break;

      for(int i = 0; i < numOfColumns; i++) {
        col--;
        elements.add(matrix[row][col]);
      }

      numOfRows--;
      if(numOfRows == 0) break;

      for(int i = 0; i < numOfRows; i++) {
        row--;
        elements.add(matrix[row][col]);
      }

      numOfColumns--;
      if(numOfColumns == 0) break;
    }

    return elements;
  }

  public static void main(String[] args) {
    int[][] test = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    SpiralMatrix travel = new SpiralMatrix();
    List<Integer> results = travel.spiralOrder(test);
    String str = Arrays.toString(results.toArray());
    System.out.println(str);
  }
}
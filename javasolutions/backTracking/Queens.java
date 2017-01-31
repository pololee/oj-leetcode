package javasolutions.backTracking;

import java.util.Arrays;

public class Queens {
  private int size;
  private int[] solution; // this array will store the solution

  public int numOfWaysToPlaceQueens(int size) {
    this.size = size;
    solution = new int[size];

    return recursiveNQueens(0);
  }

  private int recursiveNQueens(int row) {
    if (row == size) {
      System.out.format("Order of %d queens %s\n", size, Arrays.toString(solution));
      return 1;
    }

    int total = 0;
    for (int col=0; col < size; col++) {
      if (allowToPlace(row, col)) {
        solution[row] = col;
        total += recursiveNQueens(row+1);
      }
    }

    return total;
  }

  private boolean allowToPlace(int row, int col) {
    for (int i=0; i<row; i++) {
      if (solution[i] == col || Math.abs(row - i) == Math.abs(col - solution[i])) {
        return false;
      }
    }

    return true;
  }

  public static void main(String[] args) {
    Queens cal = new Queens();

    System.out.println(cal.numOfWaysToPlaceQueens(6));
    System.out.println(cal.numOfWaysToPlaceQueens(8));
  }
}
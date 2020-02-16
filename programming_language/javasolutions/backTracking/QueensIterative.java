package javasolutions.backTracking;

import java.util.Arrays;

public class QueensIterative {
  private int size;
  private int[] solution;
  private static final int INITIAL_VALUE = -1;

  public int numOfWaysToPlaceQueens(int size) {
    this.size = size;
    solution = new int[size];
    Arrays.fill(solution, INITIAL_VALUE);

    return iterativeNQueens();
  }

  private int iterativeNQueens() {
    int total = 0;
    int row = 0, col = 0;

    while(row < size) {

      while(col < size) {
        if (allowToPlace(row, col)) {
          solution[row] = col;

          col = 0; // clean col because we will move to next row
          break;
        } else {
          col++;
        }
      }

      if(solution[row] != INITIAL_VALUE && row == size - 1) { // found a solution
        total++;
        System.out.format("Order of %d queens %s\n", size, Arrays.toString(solution));

        col = solution[row] + 1; // in this row, move to the next col, enter in while(col < size) to try this col
        solution[row] = INITIAL_VALUE; // clear this row value
        continue; // stay in this row
      } else if (solution[row] == INITIAL_VALUE) {
        if (row == 0) {
          break; // game over, because in first row, we couldn't find a col to allow to place queen
        } else {
          row--; // move to the previous row
          col = solution[row] + 1; // try next col in that row
          solution[row] = INITIAL_VALUE; // clear that row's solution value
          continue; // stay in that row
        }
      }

      row++;
    }

    return total;
  }

  private boolean allowToPlace(int row, int col) {
    for (int i=0; i<row; i++) {
      if (col == solution[i] || Math.abs(row - i) == Math.abs(col - solution[i])) {
        return false;
      }
    }

    return true;
  }

  public static void main(String[] args) {
    QueensIterative cal = new QueensIterative();

    System.out.println(cal.numOfWaysToPlaceQueens(6));
  }
}
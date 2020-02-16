/**
https://leetcode.com/problems/search-a-2d-matrix-ii/#/description
 */

package javasolutions.p240;

public class SearchMatrixII {
  public boolean searchMatrix(int[][] matrix, int target) {
    if(matrix.length == 0 || matrix[0].length == 0) return false;

    int numOfRows = matrix.length;
    int numOfCols = matrix[0].length;
    if(target < matrix[0][0] || target > matrix[numOfRows-1][numOfCols-1]) return false;

    // search start from left-bottom element
    // going up -> smaller
    // going right -> bigger
    int row = matrix.length - 1;
    int col = 0;

    while(row >= 0 && col < matrix[0].length) {
      if(target > matrix[row][col]) {
        col++;
      } else if(target < matrix[row][col]) {
        row--;
      } else {
        return true;
      }
    }

    return false;
  }

  public static void main(String[] args) {
    SearchMatrixII cal = new SearchMatrixII();

    int[][] test = {{1, 4, 7, 11, 15}, {2, 5, 8, 12, 19}};
    System.out.println(cal.searchMatrix(test, 7));
    System.out.println(cal.searchMatrix(test, 0));
  }
}
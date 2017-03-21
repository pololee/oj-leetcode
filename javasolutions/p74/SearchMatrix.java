/**
https://leetcode.com/problems/search-a-2d-matrix/#/description

- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.
 */

package javasolutions.p74;

public class SearchMatrix {
  // First, find which row the target belongs to
  // Then, find the target in that row
  public boolean searchMatrix(int[][] matrix, int target) {
    if(matrix.length == 0 || matrix[0].length == 0) return false;
    if(target < matrix[0][0] || target > matrix[matrix.length - 1][matrix[0].length - 1]) return false;

    int low = 0; 
    int high = matrix.length - 1; 
    int mid = 0;

    while(low <= high) {
      mid = low + (high - low) / 2;

      if(target > matrix[mid][0]) {
        low = mid + 1;
      } else if(target < matrix[mid][0]) {
        high = mid - 1;
      } else {
        return true;
      }
    }

    // the high value will be the row that the target belongs to
    int targetRow = high;

    low = 0; 
    high = matrix[0].length - 1;
    mid = 0;
    
    while(low <= high) {
      mid = low + (high - low) / 2;

      if(target > matrix[targetRow][mid]) {
        low = mid + 1;
      } else if(target < matrix[targetRow][mid]) {
        high = mid - 1;
      } else {
        return true;
      }
    }

    return false;
  }

  public boolean anotherSearchMatrix(int[][] matrix, int target) {
    if(matrix.length == 0 || matrix[0].length == 0) return false;
    if(target < matrix[0][0] || target > matrix[matrix.length - 1][matrix[0].length - 1]) return false;

    int numOfRows = matrix.length;
    int numOfCols = matrix[0].length;
    int low = 0;
    int high = numOfRows * numOfCols - 1;
    int mid = 0;

    while(low <= high) {
      mid = low + (high - low) / 2;

      // how to convert the coordinate
      // row = index / numOfCols
      // col = index % numOfCols
      int midValue = matrix[mid / numOfCols][mid % numOfCols];
      if(target > midValue) {
        low = mid + 1;
      } else if(target < midValue) {
        high = mid - 1;
      } else {
        return true;
      }
    }
    
    return false;
  }

  public static void main(String[] args) {
    int[][] test = {{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 50}};

    SearchMatrix cal = new SearchMatrix();
    System.out.println(cal.searchMatrix(test, 3));
    System.out.println(cal.anotherSearchMatrix(test, 3));
    System.out.println(cal.searchMatrix(test, 300));
    System.out.println(cal.anotherSearchMatrix(test, 300));

    int[][] test2 = {{1, 3}};
    System.out.println(cal.anotherSearchMatrix(test2, 2));
  }
}
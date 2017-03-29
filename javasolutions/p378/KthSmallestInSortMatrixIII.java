package javasolutions.p378;

/**
Note: matrix is n * n matrix.
 */

public class KthSmallestInSortMatrixIII {
  public int kthSmallest(int[][] matrix, int k) {
    if(matrix.length == 0 || matrix[0].length == 0) return 0;

    int size = matrix.length;
    int low = matrix[0][0];
    int high = matrix[size - 1][size - 1];
    int mid = 0;
    int count = 0;

    while(low < high) {
      mid = low + (high - low) / 2;
      count = count(matrix, mid);

      if(count < k) {
        low = mid + 1;
      } else {
        high = mid;
      }
    }

    return low;
  }

  // Give the count of how many element are equal or less than target
  private int count(int[][] matrix, int target) {
    int size = matrix.length;
    int col = 0;
    int row = size - 1; // left-bottom element
    int count = 0;

    while(row >= 0 && col < size) {
      if(matrix[row][col] <= target) {
        count += (row + 1);
        col++;
      } else {
        row--;
      }
    }

    return count;
  }

  public static void main(String[] args) {
    int[][] test = {{1, 5, 9}, {10, 11, 13}, {12, 13, 15}};

    KthSmallestInSortMatrixIII cal = new KthSmallestInSortMatrixIII();
    System.out.println(cal.kthSmallest(test, 7));
  }
}
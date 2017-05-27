/**
https://leetcode.com/problems/max-sum-of-sub-matrix-no-larger-than-k/#/description
 */

package javasolutions.p363;

import java.util.TreeSet;

public class MaxSumRectangle {
  public static int maxSumSubmatrix(int[][] matrix, int k) {
    // 2D kadane algorithm https://www.youtube.com/watch?v=yCQN096CwWM
    // Find the max sum of subarray limited by K https://www.quora.com/Given-an-array-of-integers-A-and-an-integer-k-find-a-subarray-that-contains-the-largest-sum-subject-to-a-constraint-that-the-sum-is-less-than-k
    if(matrix == null || matrix.length == 0) return 0;

    int numOfRows = matrix.length, numOfCols = matrix[0].length;

    if(numOfRows < numOfCols) {
      System.out.println("num of rows is less than num of cols.");
      return rowsLessThanCols(matrix, k);
    } else {
      System.out.println("num of rows is NOT less than num of cols.");
      return colsLessThanRows(matrix, k);
    }
  }

  private static int colsLessThanRows(int[][] matrix, int k){
    int numOfRows = matrix.length, numOfCols = matrix[0].length;
    int answer = Integer.MIN_VALUE;

    for(int startCol = 0; startCol < numOfCols; startCol++) {
      int[] kadaneArray = new int[numOfRows];

      for(int endCol = startCol; endCol < numOfCols; endCol++) {
        // add endCol values to kadaneArray
        for(int i = 0; i < numOfRows; i++) {
          kadaneArray[i] += matrix[i][endCol];
        }

        // Find max sum of subarray in this kadaneArray, no larger than k
        TreeSet<Integer> cumulativeSumSet = new TreeSet<>();
        /**
        why do we need this 0?
        Look at this example: kadaneArray = {1, 0, 1}, k = 2
        So the subarray as the answer is the whole array
        which means cumulative sum ending at last index - nothing (0) is the answer
        so we need this 0, so in case we don't need to subtract anything from
        cumulativeSumEndingHere
         */
        cumulativeSumSet.add(0);
        int cumulativeSumEndingHere = 0;
        for(int j = 0; j < kadaneArray.length; j++) {
          cumulativeSumEndingHere += kadaneArray[j];

          Integer cumSumJ = cumulativeSumSet.ceiling(cumulativeSumEndingHere - k);
          if(cumSumJ != null) {
            answer = Math.max(answer, cumulativeSumEndingHere - cumSumJ);
            if(answer == k) return k;
          }

          cumulativeSumSet.add(cumulativeSumEndingHere);
        }
      }
    }

    return answer;
  }

  private static int rowsLessThanCols(int[][] matrix, int k) {
    int numOfRows = matrix.length, numOfCols = matrix[0].length;
    int answer = Integer.MIN_VALUE;

    for(int startRow = 0; startRow < numOfRows; startRow++) {
      int[] kadaneArray = new int[numOfCols];

      for(int endRow = startRow; endRow < numOfRows; endRow++) {
        // add endRow values to kadaneArray
        for(int i = 0; i < numOfCols; i++) {
          kadaneArray[i] += matrix[endRow][i];
        }

        TreeSet<Integer> cumulativeSumSet = new TreeSet<>();
        cumulativeSumSet.add(0);
        int cumulativeSumEndingHere = 0;
        for(int j = 0; j < kadaneArray.length; j++) {
          cumulativeSumEndingHere += kadaneArray[j];

          Integer cumSumJ = cumulativeSumSet.ceiling(cumulativeSumEndingHere - k);
          if(cumSumJ != null) {
            answer = Math.max(answer, cumulativeSumEndingHere - cumSumJ);
            if(answer == k) return k;
          }

          cumulativeSumSet.add(cumulativeSumEndingHere);
        }
      }
    }

    return answer;
  }

  public static void main(String[] args) {
    int[][] test = {{1,  0, 1}, {0, -2, 3}};
    System.out.println(maxSumSubmatrix(test, 2));

    int[][] test2 = {{1, 0, 1}};
    System.out.println(maxSumSubmatrix(test2, 2));
  }
}

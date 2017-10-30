/**
 * https://leetcode.com/problems/maximal-square/description/
 * Given a 2D binary matrix filled with 0's and 1's, 
 * find the largest square containing only 1's and return its area.
 * 
 * dp(i, j)=min(dp(i−1, j), dp(i−1, j−1), dp(i, j−1))+1.
 *
 */

package airbnb.p221;

public class Solution {
  public int maximalSquare(char[][] matrix) {
    int numOfRows = matrix.length;
    int numOfCols = matrix.length > 0 ? matrix[0].length : 0;

    int[][] sideLengthDP = new int[numOfRows + 1][numOfCols + 1];
    int maxSideLength = 0;

    for(int i = 1; i <= numOfRows; i++) {
      for(int j = 1; j <= numOfCols; j++) {
        if(matrix[i - 1][j - 1] == '1') {
          sideLengthDP[i][j] = Math.min(
            sideLengthDP[i-1][j-1],
            Math.min(sideLengthDP[i][j-1], sideLengthDP[i-1][j])
          ) + 1;

          maxSideLength = Math.max(maxSideLength, sideLengthDP[i][j]);
        }
      }
    }

    return maxSideLength * maxSideLength;
  }
  
  /* needs less space */
  public int maximalSquareII(char[][] matrix) {
    int numOfRows = matrix.length;
    int numOfCols = matrix.length > 0 ? matrix[0].length : 0;

    int[] sideLengthDP = new int[numOfCols + 1];
    int maxSideLength = 0;
    int prev = 0;

    for(int i = 1; i <= numOfRows; i++) {
      for(int j = 1; j <= numOfCols; j++) {
        int temp = sideLengthDP[j];

        if(matrix[i-1][j-1] == '1') {
          sideLengthDP[j] = Math.min(
            Math.min(sideLengthDP[j-1], sideLengthDP[j]),
            prev
          ) + 1;
          maxSideLength = Math.max(maxSideLength, sideLengthDP[j]);
        } else {
          sideLengthDP[j] = 0;
        }

        prev = temp;
      }
    }

    return maxSideLength * maxSideLength;
  }

  public static void main(String[] args) {
    Solution sol = new Solution();
    char[][] test = {
      { '0', '1', '1', '1', '0'},
      { '1', '1', '1', '1', '1'},
      { '0', '1', '1', '1', '1'},
      { '0', '1', '1', '1', '1'},
      { '0', '0', '1', '1', '1'}
    };

    System.out.println(sol.maximalSquare(test));
  }
}
/**
 * Given a 2D binary matrix filled with 0's and 1's,
 * find the largest rectangle containing only 1's and return its area.
 */

/**
 *
 * use the similar method as p84 largest area in histogram
 */

package facebook.p85;

import java.util.Stack;

public class Solution {
  public int maximalRectangle(char[][] matrix) {
    if(matrix.length == 0 || matrix[0].length == 0) return 0;

    int maxArea = 0;
    int currentArea = 0;
    int numOfRows = matrix.length;
    int numOfCols = matrix[0].length;
    // this is a trick. we use numOfCols + 1 as the length of the histogram heights
    // the last height is always 0, which is the lowest height
    int[] heights = new int[numOfCols + 1];

    for(int row = 0; row < numOfRows; row++) {
      Stack<Integer> stack = new Stack<>();

      for(int i = 0; i < numOfCols + 1; i++) {
        // construct the heights histogram
        if(i < numOfCols) {
          if(matrix[row][i] == '1') {
            heights[i] += 1;
          } else {
            heights[i] = 0;
          }
        }

        while(!stack.isEmpty() && heights[i] < heights[stack.peek()]) {
          int minHeightIdx = stack.pop();

          if(stack.isEmpty()) {
            currentArea = heights[minHeightIdx] * i;
          } else {
            // width = the distance between i and stack.peek()
            // i - stack.peek() - 1 because we should the count the 1 width of column i
            currentArea = heights[minHeightIdx] * (i - stack.peek() - 1);
          }

          maxArea = Math.max(maxArea, currentArea);
        }

        stack.push(i);
      }
    }

    return maxArea;
  }
}
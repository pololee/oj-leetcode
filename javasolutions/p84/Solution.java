/**
 * Given n non-negative integers representing the histogram's bar height where
 * the width of each bar is 1, find the area of largest rectangle in the histogram.
 */

package javasolutions.p84;

import java.util.Stack;

public class Solution {
  public int largestRectangleArea(int[] heights) {
    if(heights.length == 0) return 0;

    int answer = 0;
    for(int i = 0; i < heights.length; i++) {
      if(i + 1 < heights.length && heights[i] <= heights[i+1]) {
        continue;
      }

      int minHeight = heights[i];
      for(int j = i; j >= 0; j--) {
        minHeight = Math.min(minHeight, heights[j]);
        int currentArea = minHeight * (i - j + 1);
        answer = Math.max(answer, currentArea);
      }
    }

    return answer;
  }

  /**
   * http://www.geeksforgeeks.org/largest-rectangle-under-histogram/
   * For every height `x`, we calculate the area with `x` as the smallest bar
   * in the rectangle.
   * If we calculate such area with every height and find the max of all areas,
   * then we find the answer.
   */
  public int largestRectangleAreaWithStack(int[] heights) {
    if(heights.length == 0) return 0;

    // Create an empty stack. The stack holds indexes of hist[] array
    // The bars stored in stack are always in increasing order of their
    // heights.
    Stack<Integer> stack = new Stack<>();
    int top;
    int areaWithTop;
    int maxArea = 0;

    int i = 0;
    while(i < heights.length) {
      if(stack.isEmpty() || heights[i] > heights[stack.peek()]) {
        stack.push(i);
        i++;
      } else {
        top = stack.pop();
        // now height[i] < height[top], height[top] >= height[stack.peek()]
        if(stack.isEmpty()) {
          areaWithTop = heights[top] * i;
        } else {
          areaWithTop = heights[top] * (i - stack.peek() - 1);
        }

        maxArea = Math.max(maxArea, areaWithTop);
      }
    }

    // i = heights.length after the above loop, stack could be non-empty
    while(!stack.isEmpty()) {
      top = stack.pop();

      if(stack.isEmpty()) {
        areaWithTop = heights[top] * i;
      } else {
        areaWithTop = heights[top] * (i - stack.peek() - 1);
      }

      maxArea = Math.max(maxArea, areaWithTop);
    }

    return maxArea;
  }
}

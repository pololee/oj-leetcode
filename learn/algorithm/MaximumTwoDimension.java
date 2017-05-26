/**
https://www.youtube.com/watch?v=yCQN096CwWM

Maximum Sum Rectangular Submatrix in Matrix dynamic programming/2D kadane
 */

package learn.algorithm;

import java.util.Arrays;

public class MaximumTwoDimension {
  private int[][] matrix;
  private int numOfRows;
  private int numOfCols;

  public MaximumTwoDimension(int[][] matrix) {
    this.matrix = matrix;
    numOfRows = matrix.length;
    numOfCols = matrix[0].length;
  }

  public int maxSum() {
    // this is one dimensional array of the same length as num of rows of the matrix
    int[] kadaneArray = new int[numOfRows];
    // leftCol: the index of the left column of the submatrix we are computing
    // rightCol: the index of the right column of the submatrix we are computing
    int leftCol = 0, rightCol = 0;
    // maxSum: the final answer to the problem
    // currentMaxSum: store the max sum of the submatrix we are computing
    int maxSum = 0, currentMaxSum = 0;
    // maxLeft, maxRight, maxUp, maxDown
    // represent the final submatrix we found
    // maxLeft, maxRight => column indices
    // maxUp, maxDown => row indices
    int maxLeft = 0, maxRight = 0, maxUp = 0, maxDown = 0;

    for(; leftCol < numOfCols; leftCol++) {
      //Reset kadane array to be 0
      Arrays.fill(kadaneArray, 0);

      for(rightCol = leftCol; rightCol < numOfCols; rightCol++) {
        // 1. add rightCol column of the matrix (values) to kadane array
        addColumnValue(kadaneArray, rightCol);

        // 2. use kadane algorithm to find the maxSum of the kadane array and the range index
        KadaneResult kadaneAnwer = findKadaneMaxSum(kadaneArray);
        currentMaxSum = kadaneAnwer.maxSum;

        // 3. if the kadane array's maxSum' > maxSum (the final answer of the problem)
        //    update the maxSum value and the range index will be maxUp and maxDown
        //    the leftCol and rightCol will be maxLeft and maxRight
        if(currentMaxSum > maxSum) {
          maxSum = currentMaxSum;
          maxLeft = leftCol;
          maxRight = rightCol;
          maxUp = kadaneAnwer.start;
          maxDown = kadaneAnwer.end;
        }
      }
    }

    System.out.println("I found the maximum sum submatrix:");
    System.out.println("The max sum is " + maxSum);
    System.out.format("left %d, right %d, up %d, down %d\n", maxLeft, maxRight, maxUp, maxDown);

    return maxSum;
  }

  public void addColumnValue(int[] kadaneArray, int column) {
    if(column < 0 || column > numOfCols) return;

    for(int i = 0; i < numOfRows; i++) {
      kadaneArray[i] += matrix[i][column];
    }
  }

  static class KadaneResult {
    public int maxSum;
    public int start;
    public int end;

    public void print() {
      System.out.format("Kadane answer: maxSum %d, start %d, end %d\n", maxSum, start, end);
    }
  }

  public KadaneResult findKadaneMaxSum(int[] nums) {
    KadaneResult answer = new KadaneResult();

    int maxEndingHere = nums[0],
        maxSoFar = nums[0],
        maxStart = 0,
        maxEnd = 0,
        start = 0;

    for(int i = 1; i < nums.length; i++) {
      if(nums[i] > maxEndingHere + nums[i]) {
        maxEndingHere = nums[i];
        start = i;
      } else {
        maxEndingHere += nums[i];
      }

      if(maxSoFar < maxEndingHere) {
        maxSoFar = maxEndingHere;
        maxStart = start;
        maxEnd = i;
      }
    }

    answer.maxSum = maxSoFar;
    answer.start = maxStart;
    answer.end = maxEnd;

    return answer;
  }

  public static void main(String[] args) {
    int[][] test = {{1, 2, -1, -4, -20},
                    {-8, -3, 4, 2, 1},
                    {3, 8, 10, 1, 3},
                    {-4, -1, 1, 7, -6}};
    MaximumTwoDimension solver = new MaximumTwoDimension(test);

    // 1: test kadane method
    int[] testKadaneArray = {-2, -3, 4, -1, -2, 1, 5, -3};
    MaximumTwoDimension.KadaneResult kadaneTestAnswer = solver.findKadaneMaxSum(testKadaneArray);
    kadaneTestAnswer.print();

    // 2: test actual maxSum() method
    solver.maxSum();
  }
}

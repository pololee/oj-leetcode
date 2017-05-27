/**
Give an array, find the maximum sum of continuous sub array.

http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
https://www.wikiwand.com/en/Maximum_subarray_problem

Kadane's algorithm
If we know the maximum subarray sum ending at position i (maxEndingHere),
the maximum subarray sum ending at position i+1:
either the maximum subarray sum ending at position i+1 includes 
the maximum subarray sum ending at position i as a prefix, or it doesn't

Math.max(nums[i+1], maxEndingHere + nums[i+1])
 */

package learn.algorithm;

public class MaximumSubarray {
  // handle the case where all numbers are negative
  public static int maxSum(int[] nums) {
    if(nums == null || nums.length == 0) return -1;

    int maxEndingHere = nums[0], maxSoFar = nums[0];
    for(int i = 1; i < nums.length; i++) {
      maxEndingHere = Math.max(maxEndingHere + nums[i], nums[i]);
      maxSoFar = Math.max(maxSoFar, maxEndingHere);
    }

    return maxSoFar;
  }

  // handle the case where all numbers are negative
  public static int maxSumPrintRange(int[] nums) {
    if(nums == null || nums.length == 0) return -1;

    int maxEndingHere = nums[0], maxSoFar = nums[0], maxStartIdx = 0, maxEndIdx = 0, start = 0;
    for(int i = 1; i < nums.length; i++) {
      if(nums[i] > maxEndingHere + nums[i]) {
        maxEndingHere = nums[i];
        start = i;
      } else {
        maxEndingHere = maxEndingHere + nums[i];
      }

      if(maxEndingHere > maxSoFar) {
        maxSoFar = maxEndingHere;
        maxStartIdx = start;
        maxEndIdx = i;
      }
    }

    System.out.format("maxSubarray start at %d, end at %d\n", maxStartIdx, maxEndIdx);
    System.out.println("the maxsum is " + maxSoFar);
    return maxSoFar;
  }

  // The standard stupid Kadane algorithm
  // assume at least one number is positive
  public static int kadaneMaxSum(int[] nums) {
    if(nums == null || nums.length == 0) return -1;

    int maxSoFar = 0, maxEndingHere = 0;
    for(int i = 0; i < nums.length; i++) {
      maxEndingHere += nums[i];

      if(maxEndingHere < 0) {
        maxEndingHere = 0;
      } else if(maxSoFar < maxEndingHere) {
        maxSoFar = maxEndingHere;
      }
    }

    System.out.println("kadane the maxsum is " + maxSoFar);
    return maxSoFar;
  }

  // The standard stupid kadane algorithm
  // assume at least one number is positive
  public static int kadaneMaxSumPrintRange(int[] nums) {
    if(nums == null || nums.length == 0) return -1;

    int maxSoFar = 0, maxEndingHere = 0, maxStartIdx = 0, maxEndIdx = 0, start = 0;
    for(int i = 0; i < nums.length; i++) {
      maxEndingHere += nums[i];

      if(maxEndingHere < 0) {
        maxEndingHere = 0;
        start = i + 1;
      } else if(maxSoFar < maxEndingHere) {
        maxSoFar = maxEndingHere;
        maxStartIdx = start;
        maxEndIdx = i;
      }
    }

    System.out.format("kadane maxSubarray start at %d, end at %d\n", maxStartIdx, maxEndIdx);
    System.out.println("kadane the maxsum is " + maxSoFar);
    return maxSoFar;
  }

  public static void main(String[] args) {
    int[] test1 = {-2, -3, 4, -1, -2, 1, 5, -3};
    int answer1 = maxSum(test1);
    System.out.println("the answer is " + answer1);
    maxSumPrintRange(test1);
    kadaneMaxSum(test1);
    kadaneMaxSumPrintRange(test1);
    
    int[] test2 = {-2, -3, -1};
    int answer2 = maxSum(test2);
    System.out.println("the answer is " + answer2);
    maxSumPrintRange(test2);
  }
}
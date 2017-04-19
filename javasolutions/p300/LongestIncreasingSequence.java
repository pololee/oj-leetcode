/**
https://leetcode.com/problems/longest-increasing-subsequence/#/description

Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

Note: it doesn't have to be consecutive
 */

package javasolutions.p300;
import java.util.Arrays;

public class LongestIncreasingSequence {
  public int lengthOfLIS(int[] nums) {
    if(nums == null || nums.length == 0) return 0;

    // DP[i]: the length of LIS ends at element i
    int[] DP = new int[nums.length];
    for(int i= 0; i < DP.length; i++) {
      DP[i] = 1;
    }

    for(int i=1; i < nums.length; i++) {
      for(int j=0; j < i; j++) {
        if(nums[j] < nums[i]) {
          DP[i] = Math.max(DP[i], DP[j] + 1);
        }
      }
    }

    System.out.println(Arrays.toString(DP));

    int answer = 0;
    for(int i = 0; i < DP.length; i++) {
      if(DP[i] > answer) {
        answer = DP[i];
      }
    }

    return answer;
  }

  public static void main(String[] args) {
    int[] test = {10, 9, 2, 5, 3, 7, 101, 18};

    LongestIncreasingSequence cal = new LongestIncreasingSequence();
    System.out.println(cal.lengthOfLIS(test));
  }
}
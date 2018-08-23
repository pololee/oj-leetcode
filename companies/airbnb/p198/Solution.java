/**
https://leetcode.com/problems/house-robber/#/description

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that
adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were broken
into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.
 */

package airbnb.p198;

public class Solution {
  public int rob(int[] nums) {
    if(nums == null || nums.length == 0) return 0;

    // DP[i][0] means the max amount so far if we don't rob nums[i]
    // DP[i][1] means the max amount so far if we rob nums[i]
    int[][] maxAmountDP = new int[nums.length][2];
    maxAmountDP[0][1] = nums[0];

    for(int i = 1; i < nums.length; i++) {
      maxAmountDP[i][0] = Math.max(maxAmountDP[i-1][0], maxAmountDP[i-1][1]);
      maxAmountDP[i][1] = nums[i] + maxAmountDP[i-1][0];
    }

    return Math.max(maxAmountDP[nums.length-1][0], maxAmountDP[nums.length-1][1]);
  }

  public int robPro(int[] nums) {
    if(nums == null || nums.length == 0) return 0;

    int maxSoFarPrevNo = 0;
    int maxSoFarPrevYes = nums[0];

    for(int i = 1; i < nums.length; i++) {
      int temp = maxSoFarPrevNo;

      maxSoFarPrevNo = Math.max(maxSoFarPrevNo, maxSoFarPrevYes);
      maxSoFarPrevYes = temp + nums[i];
    }

    return Math.max(maxSoFarPrevNo, maxSoFarPrevYes);
  }

  public static void main(String[] args) {
    Solution sol = new Solution();
    int[] test = {2, 1, 1, 2};

    System.out.println(sol.robPro(test));
  }
}
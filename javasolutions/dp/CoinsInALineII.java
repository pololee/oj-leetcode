/**
 * There are n coins in a line. (Assume n is even).
 * Two players take turns to take a coin from one of the ends of the line until there are no more coins left.
 * The player with the larger amount of money wins.
 *
 * 1. Would you rather go first or second? Does it matter?
 * 2. Assume that you go first, describe an algorithm to compute the maximum amount of money you can win.
 *
 * Define P(i, j) as the maximum amount you can get when the remaining numbers are {Ai, Ai+1, ..., Aj}
 *
 * (Assume your opponent is NOT idiot)
 * If you pick Ai, then the maximum amount you can get is Ai + min(P(i+2,j), P(i+1, j-1))
 * If you pick Aj, then the maximum amount you can get is Aj + min(P(i+1, j-1), P(i, j-2))
 */

package javasolutions.dp;

public class CoinsInALineII {
  public int maxAmount(int[] nums) {
    if(nums.length == 0) return 0;

    int length = nums.length;
    int[][] DP = new int[length][length];

    return maxAmountHelper(nums, 0, length-1, DP);
  }

  private int maxAmountHelper(int[] nums, int start, int end, int[][] DP) {
    if(start < 0 || start > nums.length-1 || end < 0 || end > nums.length-1 || start > end) {
      return 0;
    }

    if(DP[start][end] > 0) return DP[start][end];

    if(start == end) {
      DP[start][end] = nums[start];
      return DP[start][end];
    }

    int pickNumsStartValue = nums[start] + Math.min(maxAmountHelper(nums, start+2, end, DP), maxAmountHelper(nums, start+1, end-1, DP));
    int pickNumsEndValue = nums[end] + Math.min(maxAmountHelper(nums, start+1, end-1, DP), maxAmountHelper(nums, start, end-2, DP));
    DP[start][end] = Math.max(pickNumsStartValue, pickNumsEndValue);
    return DP[start][end];
  }

  public int maxAmountIterative(int[] nums) {
    if(nums.length == 0) return 0;

    int length = nums.length;
    int[][] DP = new int[length][length];

    int startPlusTwo, startPlusOneEndMinusOne, endMinusTwo;
    int pickNumsStartValue, pickNumsEndValue;

    for (int intervalDistance=0; intervalDistance < length; intervalDistance++) {
      for (int start=0, end=intervalDistance; start<length && end<length; start++, end++) {
        if (start == end) {
          DP[start][end] = nums[start];
        } else if (start < end){
          // P(i+2, j)
          startPlusTwo = (start+2 <= end) ? DP[start+2][end] : 0;
          // P(i+1, j-1)
          startPlusOneEndMinusOne = (start+1 <= end-1) ? DP[start+1][end-1] : 0;
          // P(i, j-2)
          endMinusTwo = (start <= end-2) ? DP[start][end-2] : 0;

          pickNumsStartValue = nums[start] + Math.min(startPlusTwo, startPlusOneEndMinusOne);
          pickNumsEndValue = nums[end] + Math.min(startPlusOneEndMinusOne, endMinusTwo);

          DP[start][end] = Math.max(pickNumsStartValue, pickNumsEndValue);
        }
      }
    }

    return DP[0][length-1];
  }

  public static void main(String[] args) {
    int[] test = {3, 2, 2, 3, 1, 2};

    CoinsInALineII cal = new CoinsInALineII();
    System.out.println(cal.maxAmount(test));
    System.out.println(cal.maxAmountIterative(test));
  }
}
// There are n coins with different value in a line.
// Two players take turns to take one or two coins from left side
// until there are no more coins left.
// The player who take the coins with the most value wins.
//
// Could you please decide the first player will win or lose?
//
// Example
// Given values array A = [1,2,2], return true.
// Given A = [1,2,4], return false.
//
//
// DP[i]: the maximum value you can get starting from i to the end
//
// When at position i:
//
// Choice 1: pick nums[i], the opponent will pick nums[i+1] or (nums[i+1], nums[i+2]),
//   The opponent is not idiot. So he/she will try to make you get less values.
//   Therefore with choice 1, the final value will be nums[i] + min(DP[i+2], DP[i+3])
//
// Choice 2: pick (nums[i], nums[i+1]), same idea. the opponent choice, nums[i+2] or (nums[i+2], nums[i+3])
//   the value will be nums[i] + nums[i+1] + min(DP[i+3], DP[i+4])
//
// DP[i] = max(value1, value2) = max(nums[i] + min(DP[i+2], DP[i+3]), nums[i] + nums[i+1] + min(DP[i+3], DP[i+4]))

package javasolutions.dp;

public class CoinsInALineI {
  public boolean firstWillWin(int[] nums) {
    if(nums.length == 0) return false;

    int length = nums.length;
    if(length == 1 || length == 2) return true;


    int[] DP = new int[length];
    DP[length - 1] = nums[length - 1];
    DP[length - 2] = nums[length - 2];

    int pickOneValue, pickTwoValue;
    int dpiPlusThree, dpiPlusFour;

    for (int i = length - 3; i >= 0; i--) {
      if(i + 3 <= length - 1) {
        dpiPlusThree = DP[i+3];
      } else {
        dpiPlusThree = 0;
      }

      if(i + 4 <= length - 1) {
        dpiPlusFour = DP[i+4];
      } else {
        dpiPlusFour = 0;
      }

      pickOneValue = nums[i] + Math.min(DP[i+2], dpiPlusThree);
      pickTwoValue = nums[i] + nums[i+1] + Math.min(dpiPlusThree, dpiPlusFour);

      DP[i] = Math.max(pickOneValue, pickTwoValue);
    }

    int total = 0;
    for (int i=0; i<length; i++) {
      total += nums[i];
    }

    int opponentValue = total - DP[0];

    if (opponentValue > DP[0]) {
      return false;
    } else {
      return true;
    }
  }

  public static void main(String[] args) {
    int[] test = {1, 2, 2};

    CoinsInALineI cal = new CoinsInALineI();
    System.out.println(cal.firstWillWin(test));

    int[] test2 = {1, 2, 4};
    System.out.println(cal.firstWillWin(test2));
  }
}
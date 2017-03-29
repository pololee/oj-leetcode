/**
 * https://leetcode.com/problems/random-pick-index/?tab=Description
 */

package javasolutions.p398;

import java.util.Random;

public class RandomPickIndex {
  private int[] nums;

  public RandomPickIndex(int[] nums) {
    this.nums = nums;
  }

  public int pick(int target) {
    int answerIdx = -1;
    int count = 0;

    for (int i = 0; i < nums.length; i++) {
      if (nums[i] != target) continue;

      count++;
      if (random(count) == 0) answerIdx = i;
    }

    return answerIdx;
  }

  // generate a random number between 0 and i - 1 (both inclusive)
  private int random(int i) {
    Random rand = new Random();
    return rand.nextInt(i);
  }
}
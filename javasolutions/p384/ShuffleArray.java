/**
 * https://leetcode.com/problems/shuffle-an-array/#/description
 *
 * https://www.wikiwand.com/en/Fisher%E2%80%93Yates_shuffle
 *
 * Amazing intuitive explanation
 * http://eli.thegreenplace.net/2010/05/28/the-intuition-behind-fisher-yates-shuffling/#id5
 */

package javasolutions.p384;

import java.util.Arrays;
import java.util.Random;

public class ShuffleArray {
  public ShuffleArray(int[] nums) {
    this.nums = nums;
  }

  public int[] reset() {
    return nums;
  }

  public int[] shuffle() {
    int[] shuffled = Arrays.copyOf(nums, nums.length);

    Random rand = new Random();
    int randomNumber = 0;

    for (int i = nums.length - 1; i >= 1; i--) {
      randomNumber = rand.nextInt(i + 1);

      if (randomNumber != i) {
        int temp = shuffled[i];
        shuffled[i] = shuffled[randomNumber];
        shuffled[randomNumber] = temp;
      }
    }

    return shuffled;
  }

  private int[] nums;

  public static void main(String[] args) {
    int[] test = { 1, 2, 3, 4, 5, 6, 7, 8 };
    ShuffleArray cal = new ShuffleArray(test);
    int[] shuffled = cal.shuffle();

    System.out.println(Arrays.toString(shuffled));
  }
}
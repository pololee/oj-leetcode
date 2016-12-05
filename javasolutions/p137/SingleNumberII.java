/**
 * Given an array of integers, every element appears three times except for one.
 * Find that single one.
 *
 * Add the i-th bit of all the numbers, the sum is M
 * M mod 3 will be equal to either 0 or 1 given that every element appears three
 * times except for one.
 *
 * The result of the mod is the bit value of the single exceptional element.
 *
 *
 * 1110
 * 1110
 * 1110
 * 1001
 * _____
 * 4331    对每一位进行求和
 * 1001    对每一位的和做%3运算，来消去所有重复3次的数
 */

package javasolutions.p137;

public class SingleNumberII {
  public int singleNumber(int[] nums) {
    int[] count = new int[32];
    int result = 0;

    for (int i=0; i < 32; i++) {
      for (int j= 0; j < nums.length; j++) {
        // right shift
        int temp = (nums[j] >> i);

        // bitwise and
        if ((temp & 1) == 1) {
          count[i]++;
        }
      }

      // bitwise OR
      result = result | ((count[i] % 3) << i);
    }

    return result;
  }

  public static void main(String[] args) {
    int[] nums = {1, 1, 1, 3};

    SingleNumberII finder = new SingleNumberII();
    System.out.println(finder.singleNumber(nums));
  }
}
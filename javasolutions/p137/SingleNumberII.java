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

  // http://www.geeksforgeeks.org/find-the-element-that-appears-once/
  public int singleNumberV2(int[] nums) {
    int ones = 0, twos = 0;

    for(int i=0; i < nums.length; i++) {
      // "one & nums[i]" gives the bits that are in both 'ones' and the new element
      // Add these bits to 'twos' using OR
      twos = twos | (ones & nums[i]);

      // XOR the new element with previous 'ones' to get all bits appearing odd number of times
      ones = ones ^ nums[i];

      // The common_bit_mask are those bits which appear third time.
      // So these bits should not be there in both 'ones' and 'twos'.
      // common_bit_mask contains all these bits as 0, so that the bits can
      // be removed from 'ones' and 'twos'
      int common_bit_mask = ~(ones & twos);

      // Remove common bits (the bits that appear third time) from 'ones' and 'twos'
      ones = ones & common_bit_mask;
      twos = twos & common_bit_mask;
    }

    return ones;
  }

  public static void main(String[] args) {
    int[] nums = {1, 1, 1, 3};

    SingleNumberII finder = new SingleNumberII();
    System.out.println(finder.singleNumber(nums));
    System.out.println(finder.singleNumberV2(nums));
  }
}
package javasolutions.p421;

import java.util.Set;
import java.util.HashSet;

public class MaximumXOR {
  public int findMaximumXOR(int[] nums) {
    if (nums.length == 0) return 0;

    int max = 0, mask = 0;
    /**
     * The "max" is the record of the final result.
     *
     * You can consider this solution is greedy.
     * The greedy goal is to try to make every bit in the final result is 1, starting from left to right,
     * i.e. starting from the MSB(most significant bit)
     *
     * If max is 11100 at i = 2, it means before we reach the last two bits, 11100 is the biggest XOR result
     * we have so far. We're going to explore whether we get 1 on those two bits left.
     *
     * We start from the most significant bit
     */

    for (int i = 31; i >= 0; i--) {
      /**
       * The mast will grow like, 100...000, 110...000, then 111...111
       * It is used to get the prefix of each num
       */
      mask = mask | ( 1 << i );

      Set<Integer> prefixSet = new HashSet<>();
      for (int num : nums) {
        int prefix = num & mask;
        prefixSet.add(prefix);
      }

      /**
       * If at i = 1 and the max we have so far is 1100,
       * now we want to explore whether we could make max 1110
       */
      int greedyCandidate = max | ( 1 << i);
      for (int prefix : prefixSet) {
        /**
         * This is the most genius part.
         * We want to find a pair (a, b) that a ^ b = greedyCandidate, then we can update our max to be greedyCandidate
         * a ^ b = greedyCandidate
         *  => a ^ b ^ b = greedyCandidate ^ b and b ^ b = 0 and x ^ 0 = x
         *  => a = greedyCandidate ^ b
         *  => greedyCandidate ^ b = a
         *
         *  So if we pick b from the prefixSet, and if the prefixSet contains greedyCandidate ^ b, that means such pair
         *  exists in the prefixSet. Now we can update our max. Otherwise, don't update max and go to next bit
         */
        if (prefixSet.contains( prefix ^ greedyCandidate )) {
          max = greedyCandidate;
          break;
        }
      }
    }

    return max;
  }

  public static void main(String[] args) {
    MaximumXOR cal = new MaximumXOR();

    int[] test1 = {3, 10, 5, 25, 2, 8};
    System.out.println(cal.findMaximumXOR(test1));

    int[] test2 = {10,23,20,18,28};
    System.out.println(cal.findMaximumXOR(test2));
  }
}
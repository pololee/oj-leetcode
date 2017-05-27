/**
Given an array of integers A and an integer k,
find a subarray that contains the largest sum,
subject to a constraint that the sum is no larger than k?
 */

package learn;

import java.util.TreeSet;

public class MaximumSumNoLargerThanK {
  public static int findMax(int[] nums, int k) {
    if(nums == null || nums.length == 0) return -1;

    TreeSet<Integer> cumulativeSumSet = new TreeSet<>();
    int cumulativeSumEndingHere = 0, answer = 0;

    for(int i = 0; i < nums.length; i++) {
      cumulativeSumEndingHere += nums[i];

      /**
        nums[i] - nums[j] <= k
        nums[i] - k <= nums[j]
        https://docs.oracle.com/javase/7/docs/api/java/util/TreeSet.html#ceiling(E)
       */
      Integer leastCumSumJ = cumulativeSumSet.ceiling(nums[i] - k);
      if(leastCumSumJ != null) {
        answer = Math.max(answer, nums[i] - leastCumSumJ);
      }

      cumulativeSumSet.add(cumulativeSumEndingHere);
    }

    return answer;
  }

  public static void main(String[] args) {
    int[] test1 = {-2, -3, 4, -1, -2, 1, 5, -3};
    System.out.println(findMax(test1, 7));
  }
}
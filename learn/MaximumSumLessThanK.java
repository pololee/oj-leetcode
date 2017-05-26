/**
https://www.quora.com/Given-an-array-of-integers-A-and-an-integer-k-find-a-subarray-that-contains-the-largest-sum-subject-to-a-constraint-that-the-sum-is-less-than-k

Given an array of integers A and an integer k,
find a subarray that contains the largest sum,
subject to a constraint that the sum is less than k?
 */

package learn;

import java.util.TreeSet;

public class MaximumSumLessThanK {
  static public int findMax(int[] nums, int k) {
    if(nums == null || nums.length == 0) return -1;

    TreeSet<Integer> cumulativeSumSet = new TreeSet<>();
    int cumulativeSumEndingHere = 0, answer = 0;

    for(int i = 0; i < nums.length; i++) {
      // cumulativeSumEndingHere is the cumulative sume ending at index i
      cumulativeSumEndingHere += nums[i];

      // the sume of subarray [j+1, i] = cumSum[i] - cumSum[j]
      // The question is to find MAX(cumSum[i] - cumSum[j]) < k
      // cumSum[i] - k < cumSum[j]
      // If we can find the least element cumSum[j], which is larger than cumSum[i] - k
      // Then we find our answer, which is cumSum[i] - cumSum[j]
      // https://docs.oracle.com/javase/7/docs/api/java/util/TreeSet.html#higher(E)
      Integer leastCumSumJ = cumulativeSumSet.higher(cumulativeSumEndingHere - k);

      if(leastCumSumJ != null) {
        answer = Math.max(answer, cumulativeSumEndingHere - leastCumSumJ);
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

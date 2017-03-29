/**
 * https://leetcode.com/problems/create-maximum-number/?tab=Description
 *
 * Reference:
 * https://segmentfault.com/a/1190000007293431
 * http://blog.csdn.net/u010025211/article/details/50527279
 * https://www.hrwhisper.me/leetcode-create-maximum-number/
 *
 */

package javasolutions.p321;

import java.util.Arrays;

public class CreateMaxNumber {
  public int[] maxNumber(int[] nums1, int[] nums2, int k) {
    int[] answer = new int[k];

    for (int i = Math.max(0, k - nums2.length); i <= Math.min(k, nums1.length); i++) {
      int[] subNums1 = maxSubArray(nums1, i);
      int[] subNums2 = maxSubArray(nums2, k - i);

      int[] candidate = merge(subNums1, subNums2, k);

      if (greater(candidate, 0, answer, 0)) {
        answer = candidate;
      }
    }

    return answer;
  }


  // Given an array `nums`, select `size` elements from `nums`, so that the
  // returned subArray represent the maximum number (preserved the relative order)
  public int[] maxSubArray(int[] nums, int size) {
    int[] answer = new int[size];
    int lengthOfAnswer = 0;

    for (int i = 0; i < nums.length; i++) {

      // lengthOfAnswer represents how many elements are currently in answer
      // nums.length - i represents how many elements left in nums including nums[i]
      // if lengthOfAnswer + (nums.length - i) <= size, all the elements left have to be
      // put in the answer. Otherwise there are not enough elements to form the sub-array of size `size`.
      while ( lengthOfAnswer > 0 && lengthOfAnswer + nums.length - i > size && answer[lengthOfAnswer - 1] < nums[i] ) {
        lengthOfAnswer--;
      }

      if (lengthOfAnswer < size) {
        answer[lengthOfAnswer] = nums[i];
        lengthOfAnswer++;
      }
    }

    return answer;
  }

  public int[] merge(int[] subNums1, int[] subNums2, int k) {
    int[] answer = new int[k];

    int idxNums1 = 0, idxNums2 = 0;
    for (int i = 0; i < k; i++) {
      if (greater(subNums1, idxNums1, subNums2, idxNums2)) {
        answer[i] = subNums1[idxNums1];
        idxNums1++;
      } else {
        answer[i] = subNums2[idxNums2];
        idxNums2++;
      }
    }

    return answer;
  }

  public boolean greater(int[] subNums1, int idx1, int[] subNums2, int idx2) {
    while (idx1 < subNums1.length && idx2 < subNums2.length) {
      if (subNums1[idx1] > subNums2[idx2]) {
        // pick the element from subNums1
        return true;
      } else if ( subNums1[idx1] < subNums2[idx2] ) {
        // pick the element from subNums2
        return false;
      } else {
        // subNums1[idx1] == subNums2[idx2]
        // So compare the next position
        idx1++;
        idx2++;
      }
    }

    // Not able to pick one from the above logic.
    // pick the element from subNums1, if there is still some elements left.
    return idx1 != subNums1.length;
  }

  public static void main(String[] args) {
    CreateMaxNumber cal = new CreateMaxNumber();

    System.out.println("Test 1:");
    int[] nums1_test1 = { 3, 4, 6, 5 };
    int[] nums2_test1 = { 9, 1, 2, 5, 8, 3 };
    int k_test1 = 5;
    int[] answer_test1 = cal.maxNumber(nums1_test1, nums2_test1, k_test1);
    System.out.println(Arrays.toString(answer_test1));

    System.out.println("Test 2:");
    int[] nums1_test2 = { 6, 7 };
    int[] nums2_test2 = { 6, 0, 4 };
    int k_test2 = 5;
    int[] answer_test2 = cal.maxNumber(nums1_test2, nums2_test2, k_test2);
    System.out.println(Arrays.toString(answer_test2));

    System.out.println("Test 3:");
    int[] nums1_test3 = { 3, 9 };
    int[] nums2_test3 = { 8, 9 };
    int k_test3 = 3;
    int[] answer_test3 = cal.maxNumber(nums1_test3, nums2_test3, k_test3);
    System.out.println(Arrays.toString(answer_test3));
  }
}
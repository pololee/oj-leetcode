/**
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/#/description

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

Subscribe to see which companies asked this question.

-------------------------------------------------------
the above array rotates at index 4, value 0

 */

package javasolutions.p153;

public class Solution {
  public int findMin(int[] nums) {
    if(nums == null || nums.length == 0) return Integer.MIN_VALUE;

    int left = 0;
    int right = nums.length - 1;
    while(left < right) {
      int mid = left + (right - left) / 2;

      if(nums[mid] > nums[right]) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }

    /**
    when the loop ends, right == left == mid;
    at this mid, the first element that follows nums[mid] <= nums[right]
     */

    return nums[right];
  }

  public static void main(String[] args) {
    int[] test1 = {4, 5, 6, 7, 0, 1, 2};
    Solution cal = new Solution();
    System.out.println(cal.findMin(test1));

    int[] test2 = {9, 0, 1};
    System.out.println(cal.findMin(test2));
  }
}
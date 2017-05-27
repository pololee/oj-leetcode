/**
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/#/description

Allow duplication in the input array
 */

package javasolutions.p154;

public class Solution {
  public int findMin(int[] nums) {
    if(nums == null || nums.length == 0) return Integer.MIN_VALUE;

    int left = 0;
    int right = nums.length - 1;

    while(left < right) {
      int mid = left + (right - left) / 2;

      if(nums[mid] > nums[right]) {
        left = mid + 1;
      } else if(nums[mid] < nums[right]) {
        right = mid;
      } else if(nums[left] >= nums[mid]) {
        left++;
      } else {
        break;
      }
    }

    return nums[left];
  }

  public static void main(String[] args) {
    Solution cal = new Solution();

    int[] test1 = {1,0,1,1,1};
    System.out.println(cal.findMin(test1));

    int[] test2 = {1,1,1,0,1};
    System.out.println(cal.findMin(test2));
  }
}
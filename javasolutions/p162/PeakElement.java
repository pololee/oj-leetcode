/**
https://leetcode.com/problems/find-peak-element/#/description

since the questions say:
num[-1] = num[n] = -∞
so the peak must exist
 */

package javasolutions.p162;

public class PeakElement {
  public int findPeakElement(int[] nums) {
    if(nums == null || nums.length == 0) return Integer.MIN_VALUE;

    for(int i = 1; i < nums.length; i++) {
      if(nums[i] < nums[i-1]) return i-1;
    }

    return nums.length - 1;
  }

  public int findPeakElementBinarySearch(int[] nums) {
    if(nums == null || nums.length == 0) return Integer.MIN_VALUE;

    int left = 0;
    int right = nums.length - 1;

    while(left < right) {
      int mid = left + (right - left) / 2;

      if(nums[mid] < nums[mid + 1]) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }

    return right;
  }

  public static void main(String[] args) {
    PeakElement cal = new PeakElement();
    int[] test = {1, 2, 3};
    System.out.println(cal.findPeakElementBinarySearch(test));
  }
}
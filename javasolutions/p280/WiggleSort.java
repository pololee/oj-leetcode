/**
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].
 */
package javasolutions.p280;

import java.util.Arrays;

public class WiggleSort {
  // When i is odd number, nums[i-1] <= nums[i]
  // when i is even number, nums[i-1] >= nums[i]
  public void wiggleSort(int[] nums) {
    if(nums.length == 0) return;

    for(int i = 1; i < nums.length; i++) {
      if(( 0 == i % 2 && nums[i-1] < nums[i] ) || ( 1 == i % 2 && nums[i-1] > nums[i] )) {
        swap(nums, i-1, i);
      }
    }
  }

  private void swap(int[] nums, int a, int b) {
    int temp = nums[a];
    nums[a] = nums[b];
    nums[b] = temp;
  }

  public static void main(String[] args) {
    WiggleSort cal = new WiggleSort();

    int[] test = { 3, 5, 2, 1, 6, 4 };
    cal.wiggleSort(test);

    System.out.println(Arrays.toString(test));
  }
}
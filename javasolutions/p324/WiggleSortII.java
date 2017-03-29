/**
https://leetcode.com/problems/wiggle-sort-ii/#/description
 */

package javasolutions.p324;

import java.util.Arrays;

public class WiggleSortII {
  public void sort(int[] nums) {
    if(nums.length == 0) return;
    
    int[] copied = Arrays.copyOf(nums, nums.length);
    Arrays.sort(copied);
    
    int length = nums.length;
    int rightHalf = length - 1;
    int leftHalf = (length + 1) / 2 - 1;
    
    for(int i=0; i < length; i++) {
        if(0 == i%2) {
            nums[i] = copied[leftHalf];
            leftHalf--;
        } else {
            nums[i] = copied[rightHalf];
            rightHalf--;
        }
    }
  }

  public static void main(String[] args) {
    WiggleSortII cal = new WiggleSortII();

    int[] test = {1, 1, 1, 2, 2, 2};
    cal.sort(test);

    System.out.println(Arrays.toString(test));

    int[] test2 = {4, 5, 5, 6};
    cal.sort(test2);
    System.out.println(Arrays.toString(test2));
  }
}
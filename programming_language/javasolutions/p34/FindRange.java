/**
https://leetcode.com/problems/search-for-a-range/#/description

search for a range
 */

package javasolutions.p34;
import java.util.Arrays;

public class FindRange {
  public int[] searchRange(int[] nums, int target) {
    int[] answer = {-1, -1};

    // nums not exist
    if(nums == null || nums.length == 0) return answer;

    // binary search find the target
    int left = 0;
    int right = nums.length - 1;
    while(left < right) {
      int mid = left + (right - left) / 2;

      if(nums[mid] < target) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    /**
    when the loop finishes, 
    1. left == mid. because we increment left by 1 every time.
    2. nums[right] >= target as you can see in the else part
     */

    if(nums[right] != target) return answer;

    /**
    nums[right] == target. so nums[left] == target
    and right / left is the first element in the array that is equal to target
    as you can see in the if-else loop.

    Now we know anything below left is smaller than target.
    we need to find the first element that is larger than the target

    why right = nums.lenght?
    because this case [1, 1, 1, 8, 8] and the target is 8
     */

    answer[0] = right;
    right = nums.length;
    while(left < right) {
      int mid = left + (right - left) / 2;

      if(nums[mid] <= target) {
        left++;
      } else {
        right = mid;
      }
    }

    /**
    when the above loop finishes, nums[right] is the first element that is larger than target
     */
     answer[1] = right - 1;
     return answer;
  }

  public static void main(String[] args) {
    int[] test = {5, 7, 7, 8, 8, 10};
    FindRange cal = new FindRange();

    System.out.println(Arrays.toString(cal.searchRange(test, 8)));
  }
}
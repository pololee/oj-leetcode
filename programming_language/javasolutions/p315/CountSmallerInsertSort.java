/**
https://leetcode.com/problems/count-of-smaller-numbers-after-self/#/description

Use Insert sort
http://www.cnblogs.com/grandyang/p/5078490.html solution One
 */

package javasolutions.p315;

import java.util.List;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Arrays;

public class CountSmallerInsertSort {
  public List<Integer> countSmaller(int[] nums) {
    if(nums.length == 0) return null;

    Integer[] answer = new Integer[nums.length];
    List<Integer> sortedNums = new LinkedList<>();

    for(int i = nums.length - 1; i >= 0; i--) {
      int insertIdx = findInsertPosition(sortedNums, nums[i]);

      sortedNums.add(insertIdx, nums[i]);
      answer[i] = insertIdx;
    }

    return Arrays.asList(answer);
  }

  private int findInsertPosition(List<Integer> sortedNums, int target) {
    int low = 0, high = sortedNums.size() - 1, mid = 0;

    while(low <= high) {
      mid = low + (high - low) / 2;

      if(target > sortedNums.get(mid)) {
        low = mid + 1;
      } else if(target < sortedNums.get(mid)) {
        high = mid - 1;
      } else {
        return mid;
      }
    }

    return low;
  }

  public static void main(String[] args) {
    int[] test = {5, 2, 6, 1};

    CountSmallerInsertSort cal = new CountSmallerInsertSort();
    List<Integer> answer = cal.countSmaller(test);
    System.out.println(answer.toString());
  }
}
/**
 *
 * https://leetcode.com/problems/contains-duplicate-iii/#/description
 * Given an array of integers, find out whether there are two distinct indices i and j
 * in the array such that the absolute difference between
 * nums[i] and nums[j] is at most t
 * and the absolute difference between i and j is at most k.
 */

package airbnb.p220;

import java.util.TreeSet;

public class TreeSetSolution {
  public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
    if(k < 0 || t < 0) return false;

    TreeSet<Long> set = new TreeSet<>();
    for(int i=0; i < nums.length; i++) {
      long number = nums[i];

      if(set.floor(number) != null && number - set.floor(number) <= (long) t
        || set.ceiling(number) != null && set.ceiling(number) - number <= (long) t)
        return true;

      set.add(number);

      if(i >= k) {
        set.remove((long)nums[i-k]);
      }
    }

    return false;
  }
}

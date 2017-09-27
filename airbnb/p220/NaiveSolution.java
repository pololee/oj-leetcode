/**
 *
 * https://leetcode.com/problems/contains-duplicate-iii/#/description
 * Given an array of integers, find out whether there are two distinct indices i and j
 * in the array such that the absolute difference between 
 * nums[i] and nums[j] is at most t 
 * and the absolute difference between i and j is at most k.
 */

package airbnb.p220;

/**
 *
 * the naive solution got TLE. (time limit exceeded)
 *
 */


public class NaiveSolution {
  public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
    if(k < 0 || t < 0) return false;

    for(int i=0; i < nums.length - k - 1; i++) {
      for(int j = i + 1; j <= i + k && j < nums.length; j++) {
        long a = nums[i];
        long b = nums[j];

        if(Math.abs(a - b) <= (long) t) return true;
      }
    }

    return false;
  }
}


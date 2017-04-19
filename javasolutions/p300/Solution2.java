/**
https://leetcode.com/problems/longest-increasing-subsequence/#/description

Some good explanantion

https://segmentfault.com/a/1190000003819886
http://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/

Our strategy determined by the following conditions,

If A[i] is smallest among all end
candidates of active lists, we will start
new active list of length 1.

If A[i] is largest among all end candidates of
active lists, we will clone the largest active
list, and extend it by A[i].

If A[i] is in between, we will find a list with
largest end element that is smaller than A[i].
Clone and extend this list by A[i]. We will discard all
other lists of same length as that of this modified list."

    public int lengthOfLIS(int[] nums) {
        int len = nums.length;
        if(len==0) return 0;
        int[] table = new int[len];
        table[0] = nums[0];
        int res = 1;
        for(int i = 1; i < len ; i++){
            if(nums[i]<table[0]){
                table[0] = nums[i];
            }
            else if(nums[i]>table[res-1]){
                table[res++] = nums[i];
            }
            else table[ceil(table,nums[i],res-1)] = nums[i];
        }
        return res;
    }
    
    private int ceil(int[] t, int target,int len) {
        int lo = 0, hi = len, mid;
        while(lo<hi) {
            mid = (lo + hi)/2;
            if(t[mid]<target) lo = mid + 1;
            else hi = mid;
        }
        return hi;
    }
}
 */

package javasolutions.p300;

public class Solution2 {
  public int lengOfLIS(int[] nums) {
    if(nums == null || nums.length == 0) return 0;

    int[] tails = new int[nums.length];
    tails[0] = nums[0];
    int size = 1;

    for(int i = 1; i < nums.length; i++) {
      if(nums[i] < tails[0]) {
        tails[0] = nums[i];
      } else if(nums[i] > tails[size - 1]) {
        // Note: this questions is asking increasing, not non-decreasing sequence
        tails[size] = nums[i];
        size++;
      } else {
        int position = binarySearch(tails, 0, size - 1, nums[i]);
        tails[position] = nums[i];
      }
    }

    return size;
  }

  private int binarySearch(int[] tails, int left, int right, int target) {
    while(left <= right) {
      int middle = left + (right - left) / 2;

      if(tails[middle] == target) {
        return middle;
      } else if(tails[middle] < target) {
        left = middle + 1;
      } else {
        right = middle - 1;
      }
    }

    return left; // where the target should be
  }

  public static void main(String[] args) {
    int[] test = {10, 9, 2, 5, 3, 7, 101, 18};
    Solution2 cal = new Solution2();
    System.out.println(cal.lengOfLIS(test));
  }
}
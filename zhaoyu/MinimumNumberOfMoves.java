import java.util.*;
import java.io.*;
import java.math.*;
import java.text.*;

public class Test {

 public static void main(String[] args) {
  // TODO Auto-generated method stub
  Solution szy = new Solution();
  int[] nums = {1,1,5,2,2};
        System.out.print(szy.Minimumcost(nums));
        
 }
 
}

class Solution {
     public int Minimumcost(int[] nums) {
      if (nums == null || nums.length == 0) {
       return 0;
      }
      
      int increase = helper(nums);
      reverse(nums);
      int decrease = helper(nums);
      
      return Math.min(increase, decrease);
     }
     public int helper(int[] a) {
      int len = a.length;
      int[] b = Arrays.copyOf(a, len);
      Arrays.sort(b);
      
      int[][] dp = new int[len][len];
      dp[0][0] = Math.abs(a[0] - b[0]);
      
      for (int i = 1; i < len; i ++) {
       dp[i][0] = dp[i - 1][0] + Math.abs(a[i]-b[0]);
      }
      
      for (int i = 1; i < len; i++) {
       dp[0][i] = Math.min(dp[0][i - 1],  Math.abs(a[0] - b[i]));
      }
      
      for(int i = 1; i < len; i++) {
       for (int j = 1; j < len; j++) {
        dp[i][j] = Math.min(dp[i - 1][j] + Math.abs(a[i] - b[j]), dp[i][j - 1]);
       }
      }
      
      return dp[len - 1][len - 1];
      
     }
     
     public void reverse(int[] nums) {
      int left = 0;
      int right = nums.length - 1;
      while (left < right) {
       int tmp = nums[left];
       nums[left] = nums[right];
       nums[right] = tmp;
       left ++;
       right --;
      }
     }
}

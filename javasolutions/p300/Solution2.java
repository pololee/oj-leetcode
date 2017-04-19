package javasolutions.p300;

public class Solution2 {
  public int lengOfLIS(int[] nums) {
    if(nums == null || nums.length == 0) return 0;
  }

  public static void main(String[] args) {
    int[] test = {10, 9, 2, 5, 3, 7, 101, 18};
    Solution2 cal = new Solution2();
    System.out.println(cal.lengOfLIS(test));
  }
}
package javasolutions.p53;

public class MaximumSubarray {
  // https://en.wikipedia.org/wiki/Maximum_subarray_problem
  // Kadane's algorithm
  public int maxSubArray(int[] nums) {
    if(nums.length == 0) return 0;
    int maxEndingHere = nums[0], maxSoFar = nums[0];

    for (int i=1; i<nums.length; i++) {
      maxEndingHere = Math.max(maxEndingHere + nums[i], nums[i]);
      if(maxEndingHere > maxSoFar) maxSoFar = maxEndingHere;
    }

    return maxSoFar;
  }

  public static void main(String[] args) {
    int[] test = {-2,1,-3,4,-1,2,1,-5,4};

    MaximumSubarray cal = new MaximumSubarray();

    System.out.println(cal.maxSubArray(test));
  }
}
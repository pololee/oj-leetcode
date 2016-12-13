package javasolutions.p152;

public class MaximumProductSubarray {
  public int maxProduct(int[] nums) {
    if(nums.length == 0) return 0;

    int maxEndingHere = nums[0], minEndingHere = nums[0], maxSoFar = nums[0];

    int bigger = 0, smaller = 0, prevMaxEndingHere;
    for(int i=1; i<nums.length; i++) {
      prevMaxEndingHere = maxEndingHere;

      bigger = Math.max(prevMaxEndingHere * nums[i], minEndingHere * nums[i]);
      maxEndingHere = Math.max(bigger, nums[i]);

      smaller = Math.min(prevMaxEndingHere * nums[i], minEndingHere * nums[i]);
      minEndingHere = Math.min(smaller, nums[i]);

      if(maxEndingHere > maxSoFar) maxSoFar = maxEndingHere;
    }

    return maxSoFar;
  }

  public static void main(String[] args) {
    int[] test = {2,3,-2,4};
    MaximumProductSubarray cal = new MaximumProductSubarray();
    System.out.println(cal.maxProduct(test));
  }
}
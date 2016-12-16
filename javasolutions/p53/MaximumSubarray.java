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

  public int maxSubArrayDivideAndConquer(int[] nums) {
    if(nums.length == 0) return 0;

    return maxSubArrayDivideAndConquerHelper(nums, 0, nums.length - 1);
  }

  private int maxSubArrayDivideAndConquerHelper(int[] nums, int leftIndex, int rightIndex) {
    if(leftIndex > rightIndex) return Integer.MIN_VALUE;

    int middleIndex = (leftIndex + rightIndex)/2;

    int leftMaxSum = 0;
    int sum = 0;
    for(int i=middleIndex-1; i>=leftIndex; i--) {
      sum += nums[i];
      if(sum > leftMaxSum) leftMaxSum = sum;
    }

    int rightMaxSum = 0;
    sum = 0;
    for(int i=middleIndex+1; i<=rightIndex; i++) {
      sum += nums[i];
      if(sum > rightMaxSum) rightMaxSum = sum;
    }

    int leftAnswer = maxSubArrayDivideAndConquerHelper(nums, leftIndex, middleIndex-1);
    int rightAnswer = maxSubArrayDivideAndConquerHelper(nums, middleIndex+1, rightIndex);
    int biggerAnswer = Math.max(leftAnswer, rightAnswer);
    return Math.max(leftMaxSum+nums[middleIndex]+rightMaxSum, biggerAnswer);
  }

  public static void main(String[] args) {
    int[] test = {-2,1,-3,4,-1,2,1,-5,4};

    MaximumSubarray cal = new MaximumSubarray();

    System.out.println(cal.maxSubArray(test));
    System.out.println(cal.maxSubArrayDivideAndConquer(test));
  }
}
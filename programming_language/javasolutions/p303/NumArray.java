package javasolutions.p303;

public class NumArray {
  private int[] sumDP;

  public NumArray(int[] nums) {
    int length = nums.length;

    sumDP = new int[length+1];
    for (int i=1; i<=length; i++) {
      sumDP[i] = nums[i-1] + sumDP[i-1];
    }
  }

  public int sumRange(int i, int j) {
    if(i > j || i < 0 || j < 0 || i >= sumDP.length || j >= sumDP.length) return 0;

    return sumDP[j+1] - sumDP[i];
  }

  public static void main(String[] args) {
    int[] test = {-2, 0, 3, -5, 2, -1};
    NumArray numArray = new NumArray(test);

    System.out.println(numArray.sumRange(0, 2));
    System.out.println(numArray.sumRange(2, 5));
  }
}
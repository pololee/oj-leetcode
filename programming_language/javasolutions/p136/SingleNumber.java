package javasolutions.p136;

public class SingleNumber {
  public int findSingleNumber(int[] nums) {
    int number = 0;

    for (int i=0; i < nums.length; i++) {
      number ^= nums[i];
    }

    return number;
  }
}
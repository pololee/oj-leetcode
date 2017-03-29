public class BubbleSort {
  public static void sort(int[] nums) {
    if(nums.length == 0) return;

    int lastIdx = nums.length - 1;
    boolean swap = true;

/**
if in one round, there is no swap happened. That means
all the nums are in right order. no need to enter the loop again.

Complexity:
Time O(n^2): (1 + 2 + ...+ (n-1)) comparison
Space O(1)
 */
    while(lastIdx > 0 && swap) {
      swap = false;

      for(int i = 0; i < lastIdx; i++) {
        if(nums[i] > nums[i+1]) {
          swap = true;

          int temp = nums[i];
          nums[i] = nums[i+1];
          nums[i+1] = temp;
        }
      }

      lastIdx--;
    }
  }

  public static void main(String[] args) {
    int[] test = {20,30,40,90,50,60,70,80,100,110};
    BubbleSort.sort(test);

    for (int i=0; i<test.length; i++) {
      System.out.format("%d, ", test[i]);
    }

    System.out.println();
  }
}
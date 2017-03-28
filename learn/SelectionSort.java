public class SelectionSort {
  public static void sort(int[] nums) {
    if(nums.length == 0) return;

    int length = nums.length;
    for(int toBefilledPosition = length - 1; toBefilledPosition > 0; toBefilledPosition--) {
      int positionOfMax = 0;

/**
key point: each round find the maximum among [0, toBefilledPosition]
swap this maximum with nums[toBefilledPosition]

Complexity:
Time: O(n^2)
Space: O(1)
 */

      for(int i = 0; i <= toBefilledPosition; i++) {
        if(nums[positionOfMax] < nums[i]) {
          positionOfMax = i;
        }
      }

      int temp = nums[toBefilledPosition];
      nums[toBefilledPosition] = nums[positionOfMax];
      nums[positionOfMax] = temp;
    }
  }
}
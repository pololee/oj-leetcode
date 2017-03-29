import java.util.Arrays;

public class ShellSort {
  public static void sort(int[] nums) {
    int subListSize = nums.length / 2;

/**
use gap to split the whole list into sublist 
perform insertion sort on each sublist
the final sublist size is 1, which will the normal insertion sort
 */
    while(subListSize > 0) {
      for(int i = 0; i < subListSize; i++) {
        gapInsertionSort(nums, i, subListSize);
      }

      System.out.format("sublist size: %d\n", subListSize);
      System.out.println("list: "+ Arrays.toString(nums));

      subListSize = subListSize / 2;
    }
  }

  private static void gapInsertionSort(int[] nums, int start, int gap) {
    for(int i = start + gap; i < nums.length; i += gap) {
      int currentValue = nums[i];
      int position = i;

      while(position >= gap && currentValue < nums[position - gap]) {
        nums[position] = nums[position - gap];
        position = position - gap;
      }

      nums[position] = currentValue;
    }
  }

  public static void main(String[] args) {
    int[] test = {54,26,93,17,77,31,44,55,20};

    ShellSort.sort(test);
  }
}
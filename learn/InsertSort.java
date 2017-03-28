public class InsertSort {
  public static void sort(int[] nums) {
    for(int i = 1; i < nums.length; i++) {
/**
the nums before position are sorted.
Insert nums[position] to the sorted list.
 */
      int currentValue = nums[i];
      int position = i;

/**
when the while loop stops, the position is where currentValue should be
 */
      while(position > 0 && currentValue < nums[position - 1]) {
        nums[position] = nums[position - 1];
        position--;
      }

      nums[position] = currentValue;
    }
  }

/**
Complexity:
Time: O(n^2)
best case: 
in the best case, only one comparison needs to be done on each pass. 
This would be the case for an already sorted list.
 */
  public static void main(String[] args) {
    int[] test = {54,26,93,17,77,31,44,55,20};
    InsertSort.sort(test);

    for (int i=0; i<test.length; i++) {
      System.out.format("%d, ", test[i]);
    }

    System.out.println();
  }
}
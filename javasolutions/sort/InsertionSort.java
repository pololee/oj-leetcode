package javasolutions.sort;

public class InsertionSort {
  public void sort(int[] nums) {
    int length = nums.length;

    for (int i=1; i<length; i++) {
      int current = nums[i];
      int position = i;

      while (position > 0 && nums[position-1] > current) {
        nums[position] = nums[position-1];
        position--;
      }

      nums[position] = current;
    }
  }

  public static void main(String[] args) {
    int[] test = {54,26,93,17,77,31,44,55,20};

    InsertionSort cal = new InsertionSort();
    cal.sort(test);

    for (int i=0; i<test.length; i++) {
      System.out.format("%d, ", test[i]);
    }

    System.out.println();
  }
}
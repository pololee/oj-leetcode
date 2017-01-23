package javasolutions.sort;

public class ShellSort {
  public void sort(int[] nums) {
    int gap = nums.length / 2;

    while(gap > 0) {
      for (int i=0; i<gap; i++) {
        gapInsertionSort(nums, i, gap);
      }

      System.out.format("gap %d\n", gap);
      print(nums);

      gap = gap / 2;
    }
  }

  private void gapInsertionSort(int[] nums, int start, int gap) {
    for (int i=start+gap; i<nums.length; i += gap) {
      int currentValue = nums[i];
      int position = i;

      while (position > start && nums[position-gap] > currentValue) {
        nums[position] = nums[position-gap];
        position -= gap;
      }

      nums[position] = currentValue;
    }
  }

  private void print(int[] nums) {
    System.out.print(nums[0]);

    for (int i=1; i<nums.length; i++) {
      System.out.format(", %d", nums[i]);
    }

    System.out.println();
  }

  public static void main(String[] args) {
    int[] test = {54,26,93,17,77,31,44,55,20};

    ShellSort cal = new ShellSort();
    cal.sort(test);
  }
}
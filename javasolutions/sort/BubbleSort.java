package javasolutions.sort;

public class BubbleSort {
  public void sort(int[] nums) {
    boolean swap = true;
    int lastIdx = nums.length - 1;

    while (lastIdx > 0 && swap) {
      System.out.println(lastIdx);
      swap = false;
      for (int i=0; i<lastIdx; i++) {
        if (nums[i] > nums[i+1]) {
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
    BubbleSort cal = new BubbleSort();
    cal.sort(test);

    for (int i=0; i<test.length; i++) {
      System.out.format("%d, ", test[i]);
    }

    System.out.println();
  }
}
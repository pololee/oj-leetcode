package javasolutions.sort;

public class SelectionSort {
  public void sort(int[] nums) {
    int length = nums.length;

    for (int toBeFilledPosition=length-1; toBeFilledPosition>0; toBeFilledPosition--) {
      int positionOfMax = 0;

      for (int i=1; i<=toBeFilledPosition; i++) {
        if (nums[i] > nums[positionOfMax]) {
          positionOfMax = i;
        }
      }

      int temp = nums[toBeFilledPosition];
      nums[toBeFilledPosition] = nums[positionOfMax];
      nums[positionOfMax] = temp;
    }
  }

  public static void main(String[] args) {
    int[] test = {54,26,93,17,77,31,44,55,20};

    SelectionSort cal = new SelectionSort();
    cal.sort(test);

    for (int i=0; i<test.length; i++) {
      System.out.format("%d, ", test[i]);
    }

    System.out.println();
  }
}
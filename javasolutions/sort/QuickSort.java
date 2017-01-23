package javasolutions.sort;

import java.util.Arrays;

public class QuickSort {
  public void sort(int[] nums) {
    quickSort(nums, 0, nums.length - 1);
  }

  private void quickSort(int[] nums, int first, int last) {
    if (first < last) {
      int splitPoint = partition(nums, first, last);

      quickSort(nums, first, splitPoint-1);
      quickSort(nums, splitPoint + 1, last);
    }
  }

  private int partition(int[] nums, int first, int last) {
    int pivotValue = nums[first];

    int leftMark = first + 1, rightMark = last;
    boolean done = false;

    while (!done) {
      while (leftMark <= rightMark && nums[leftMark] <= pivotValue) {
        leftMark++;
      }

      while (rightMark >= leftMark && nums[rightMark] >= pivotValue) {
        rightMark--;
      }

      if (leftMark > rightMark) {
        done = true;
      } else {
        swap(nums, leftMark, rightMark);
      }
    }

    swap(nums, first, rightMark);

    return rightMark;
  }

  private void swap(int[] nums, int a, int b) {
    int temp = nums[a];
    nums[a] = nums[b];
    nums[b] = temp;
  }

  public static void main(String[] args) {
    int[] test = {54,26,93,17,77,31,44,55,20};

    QuickSort cal = new QuickSort();
    cal.sort(test);
    System.out.println(Arrays.toString(test));
  }
}
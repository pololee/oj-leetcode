package javasolutions.sort;

import java.util.Arrays;

public class MergeSort {
  private int[] temp;

  public void sort(int[] nums) {
    temp = new int[nums.length];

    mergeSort(nums, 0, nums.length-1);
  }

  private void mergeSort(int[] nums, int start, int end) {
    if(start < end) {
      int middle = start + (end - start) / 2;
      mergeSort(nums, start, middle);
      mergeSort(nums, middle + 1, end);

      merge(nums, start, middle + 1, end);
    }
  }

  private void merge(int[] nums, int leftStart, int rightStart, int rightEnd) {
    int leftEnd = rightStart - 1;
    int leftIdx = leftStart;
    int rightIdx = rightStart;

    int index = 0, length = rightEnd - leftStart + 1;

    while(leftIdx <= leftEnd && rightIdx <= rightEnd) {
      if(nums[leftIdx] < nums[rightIdx]) {
        temp[index] = nums[leftIdx];
        leftIdx++;
      } else {
        temp[index] = nums[rightIdx];
        rightIdx++;
      }

      index++;
    }

    while(leftIdx <= leftEnd) {
      temp[index] = nums[leftIdx];
      leftIdx++;
      index++;
    }

    while(rightIdx <= rightEnd) {
      temp[index] = nums[rightIdx];
      rightIdx++;
      index++;
    }

    for (int i=0; i<length; i++) {
      nums[leftStart + i] = temp[i];
    }
  }

  public static void main(String[] args) {
    int[] test = {54,26,93,17,77,31,44,55,20};

    MergeSort cal = new MergeSort();
    cal.sort(test);

    System.out.println(Arrays.toString(test));
  }
}
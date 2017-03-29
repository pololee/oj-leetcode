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

      merge(nums, start, end);
    }
  }

  private void merge(int[] nums, int start, int end) {
    int middle = start + (end - start)/2;

    int leftIdx = start;
    int rightIdx = middle + 1;

    int index = 0, length = end - start + 1;

    while(leftIdx <= middle && rightIdx <= end) {
      if(nums[leftIdx] < nums[rightIdx]) {
        temp[index] = nums[leftIdx];
        leftIdx++;
      } else {
        temp[index] = nums[rightIdx];
        rightIdx++;
      }

      index++;
    }

    while(leftIdx <= middle) {
      temp[index] = nums[leftIdx];
      leftIdx++;
      index++;
    }

    while(rightIdx <= end) {
      temp[index] = nums[rightIdx];
      rightIdx++;
      index++;
    }

    for (int i=0; i<length; i++) {
      nums[start + i] = temp[i];
    }
  }

  public static void main(String[] args) {
    int[] test = {54,26,93,17,77,31,44,55,20};

    MergeSort cal = new MergeSort();
    cal.sort(test);

    System.out.println(Arrays.toString(test));
  }
}
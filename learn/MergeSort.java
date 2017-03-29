/**

This version needs extra space.
You can do in-place merge sort, which is not trivial.

http://stackoverflow.com/questions/2571049/how-to-sort-in-place-using-the-merge-sort-algorithm
https://github.com/liuxinyu95/AlgoXY chapter 13

Time complexity:
O(nlogn)

 */

import java.util.Arrays;

public class MergeSort {
  private int[] temp;

  public void sort(int[] nums) {
    temp = new int[nums.length];
    mergeSort(nums, 0, nums.length - 1);
  }

  private void mergeSort(int[] nums, int start, int end) {
    if(start < end) {
      System.out.format("Splitting: start: %d, end: %d\n", start, end);
      System.out.println(Arrays.toString(nums));


      int middle = start + (end - start) / 2;

      mergeSort(nums, start, middle);
      mergeSort(nums, middle + 1, end);

      merge(nums, start, middle + 1, end);

      System.out.format("Merging: start: %d, middle+1: %d, end: %d\n", start, middle+1, end);
      System.out.println(Arrays.toString(nums));
    }
  }

  private void merge(int[] nums, int leftStart, int rightStart, int rightEnd) {
    int leftIdx = leftStart;
    int rightIdx = rightStart;
    int leftEnd = rightStart - 1;

    int idx = 0;
    int length = rightEnd - leftStart + 1;

    while(leftIdx <= leftEnd && rightIdx <= rightEnd) {
      if(nums[leftIdx] < nums[rightIdx]) {
        temp[idx] = nums[leftIdx];
        leftIdx++;
      } else {
        temp[idx] = nums[rightIdx];
        rightIdx++;
      }

      idx++;
    }

    while(leftIdx <= leftEnd) {
      temp[idx] = nums[leftIdx];
      leftIdx++;
      idx++;
    }

    while(rightIdx <= rightEnd) {
      temp[idx] = nums[rightIdx];
      rightIdx++;
      idx++;
    }

    System.arraycopy(temp, 0, nums, leftStart, length);
  }

  public static void main(String[] args) {
    int[] test = {54,26,93,17,77,31,44,55,20};

    MergeSort cal = new MergeSort();
    cal.sort(test);

    System.out.println(Arrays.toString(test));
  }
}
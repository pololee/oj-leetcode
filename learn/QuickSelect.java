/**
https://gist.github.com/unnikked/14c19ba13f6a4bfd00a3

Find the k-th smallest number in a list

K-th smallest means in the sorted list, there are k-1
numbers that are less than the k-th smallest number,
which means the index of the k-th smallest number is k-1

 */

import java.util.Arrays;

public class QuickSelect {
  public static int selectIterative(int[] nums, int k) {
    if(k > nums.length) return Integer.MAX_VALUE;

    return iterative(nums, 0, nums.length - 1, k);
  }

  private static int iterative(int[] nums, int left, int right, int k) {
    if(left == right) {
      return nums[left];
    }

    while(true) {
      int pivotIndex = randomPivot(left, right);
      pivotIndex = partition(nums, left, right, pivotIndex);

      if(pivotIndex == k - 1) {
        return nums[pivotIndex];
      } else if( pivotIndex > k - 1 ) {
        right = pivotIndex - 1;
      } else {
        left = pivotIndex + 1;
      }
    }
  }

  public static int selectRecursive(int[] nums, int k) {
    if(k > nums.length) return Integer.MAX_VALUE;

    return recursive(nums, 0, nums.length - 1, k);
  }

  private static int recursive(int[] nums, int left, int right, int k) {
    if(left == right) {
      return nums[left];
    }

    int pivotIndex = randomPivot(left, right);
    pivotIndex = partition(nums, left, right, pivotIndex);

    if(pivotIndex == k - 1) {
      return nums[pivotIndex];
    } else if(pivotIndex > k - 1) {
      return recursive(nums, left, pivotIndex - 1, k);
    } else {
      return recursive(nums, pivotIndex + 1, right, k);
    }
  }

  private static int partition(int[] nums, int left, int right, int pivotIndex) {
    int pivotValue = nums[pivotIndex];
    swap(nums, pivotIndex, right); // move the pivot to end

    int storeIndex = left;
    for(int i = left; i < right; i++) {
      if(nums[i] < pivotValue) {
        swap(nums, i, storeIndex);
        storeIndex++;
      }
    }

    swap(nums, storeIndex, right); // move pivot to its final place
    return storeIndex; // the index of the pivot
  }

  private static void swap(int[] nums, int a, int b) {
    if(a == b) return;

    int temp = nums[a];
    nums[a] = nums[b];
    nums[b] = temp;
  }

  private static int randomPivot(int left, int right) {
    return left + (int) Math.floor(Math.random() * (right - left + 1));
  }

  public static void main(String[] args) {
    int[] test = {9, 8, 7, 6, 5, 0, 1, 2, 3, 4};

    System.out.println("Test Array: " + Arrays.toString(test));
    System.out.println();
    System.out.println("Use iterative method:");
    for(int i = 1; i <= test.length; i++) {
      System.out.format("The %d-th smallest number: %d\n", i, selectIterative(test, i));
    }

    System.out.println();
    System.out.println("Use recursive method:");
    for(int i = 1; i <= test.length; i++) {
      System.out.format("The %d-th smallest number: %d\n", i, selectRecursive(test, i));
    }
  }
}
 package javasolutions.p315;

import java.util.List;
import java.util.ArrayList;

public class CountSmaller {
  private int[] count;
  private int[] inputNums;
  private int[] indices;

  public List<Integer> countSmaller(int[] nums) {
    List<Integer> result = new ArrayList<Integer>();

    inputNums = nums;
    count = new int[nums.length];

    indices = new int[nums.length];
    for (int i=0; i<indices.length; i++) {
      indices[i] = i;
    }

    mergeSort(0, nums.length - 1);

    for (int i=0; i<count.length; i++) {
      result.add(count[i]);
    }

    return result;
  }

  private void mergeSort(int start, int end) {
    if(start < end) {
      int middle = start + (end - start) / 2;

      mergeSort(start, middle);
      mergeSort(middle + 1, end);

      merge(start, end);
    }
  }

  private void merge(int start, int end) {
    int middle = start + (end - start) / 2;

    int leftIndex = start;
    int rightIndex = middle + 1;

    int rightCount = 0;
    int[] tempIndices = new int[end - start + 1];

    int index = 0;
    while (leftIndex <= middle && rightIndex <= end) {
      if (inputNums[indices[rightIndex]] < inputNums[indices[leftIndex]]) {
        tempIndices[index] = indices[rightIndex];
        rightCount++;
        rightIndex++;
      } else {
        tempIndices[index] = indices[leftIndex];
        count[indices[leftIndex]] += rightCount;
        leftIndex++;
      }

      index++;
    }

    while (leftIndex <= middle) {
      tempIndices[index] = indices[leftIndex];
      count[indices[leftIndex]] += rightCount;
      leftIndex++;
      index++;
    }

    while (rightIndex <= end) {
      tempIndices[index] = indices[rightIndex];
      rightIndex++;
      index++;
    }

    for (int i=0; i<tempIndices.length; i++) {
      indices[start + i] = tempIndices[i];
    }
  }

  public static void main(String[] args) {
    int[] test = {5, 2, 6, 1};

    CountSmaller cal = new CountSmaller();

    List<Integer> answer = cal.countSmaller(test);

    for (Integer x : answer) {
      System.out.println(x);
    }
  }
}
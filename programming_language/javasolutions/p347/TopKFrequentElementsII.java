/**
https://leetcode.com/problems/top-k-frequent-elements/#/description
 */

package javasolutions.p347;

import java.util.*;

public class TopKFrequentElementsII {
  public List<Integer> topKElements(int[] nums, int k) {
    List<Integer> answer = new ArrayList<>();
    if(nums == null || nums.length == 0 || k <= 0) return answer;

    // construct frequency mapping
    Map<Integer, Integer> frequencyMap = new HashMap<>();
    for(int num: nums) {
      if(!frequencyMap.containsKey(num)) frequencyMap.put(num, 0);

      frequencyMap.put(num, frequencyMap.get(num) + 1);
    }

    // check if there are at least k distinct numbers
    if(frequencyMap.size() < k) return answer;

    List<Map.Entry<Integer, Integer>> list = new ArrayList<>(frequencyMap.entrySet());
    int left = 0;
    int right = list.size() - 1;

    while(true) {
      int pivotIndex = partition(list, left, right);

      if(pivotIndex + 1 == k) {
        break;
      } else if(pivotIndex + 1 > k) {
        right = pivotIndex - 1;
      } else {
        left = pivotIndex + 1;
      }
    }

    for(int i = 0; i < k; i++) {
      answer.add(list.get(i).getKey());
    }

    return answer;
  }

  private int partition(List<Map.Entry<Integer, Integer>> list, int left, int right) {
    int pivotIndex = randomPivot(left, right);
    int pivotValue = list.get(pivotIndex).getValue();
    swap(list, pivotIndex, right);

    int leftMark = left;
    int rightMark = right - 1;

    while(true) {
      while(leftMark <= rightMark && list.get(leftMark).getValue() >= pivotValue) {
        leftMark++;
      }

      while(rightMark >= leftMark && list.get(rightMark).getValue() <= pivotValue) {
        rightMark--;
      }

      if(leftMark > rightMark) {
        break;
      } else {
        swap(list, leftMark, rightMark);
      }
    }

    swap(list, right, leftMark);
    return leftMark;
  }

  private int randomPivot(int left, int right) {
    return new Random().nextInt(right - left + 1) + left;
  }

  private void swap(List<Map.Entry<Integer, Integer>> list, int a, int b) {
    if(a == b) return;

    Map.Entry<Integer, Integer> temp = list.get(a);
    list.set(a, list.get(b));
    list.set(b, temp);
  }

  public static void main(String[] args) {
    int[] nums = {1, 1, 1, 2, 2, 3};

    TopKFrequentElementsII cal = new TopKFrequentElementsII();
    System.out.println(Arrays.toString(cal.topKElements(nums, 2).toArray()));
  }
}
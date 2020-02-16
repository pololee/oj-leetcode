/**
https://leetcode.com/problems/top-k-frequent-elements/#/description
*/

package javasolutions.p347;

import java.util.*;

public class TopKFrequentElements {
  public List<Integer> topKFrequent(int[] nums, int k) {
    List<Integer> result = new ArrayList<>();
    if (nums == null || nums.length == 0 || k <= 0) return result;
    
    Map<Integer, Integer> map = new HashMap<>();
    
    for (int num : nums) {
        if (!map.containsKey(num)) map.put(num, 0);
        map.put(num, map.get(num) + 1);
    }
    
    if (map.size() < k) return result;
    
    List<Map.Entry<Integer, Integer>> list = new ArrayList<>(map.entrySet());
    
    int left = 0;
    int right = list.size() - 1;
    
    while (true) {
        int pos = partition(list, left, right);
        
        if (pos + 1 == k) {
            break;
        } else if (pos + 1 > k) {
            right = pos - 1;
        } else {
            left = pos + 1;
        }
    }
    
    for (int i = 0; i < k; i++) {
        result.add(list.get(i).getKey());
    }
    
    return result;
  }
  
  private int partition(List<Map.Entry<Integer, Integer>> list, int left, int right) {
    int index = new Random().nextInt(right - left + 1) + left;
    int pivotVal = list.get(index).getValue();
    
    swap(list, left, index);
    
    int start = left + 1;
    int end = right;
    
    while (start <= end) {
        if (list.get(start).getValue() < pivotVal && list.get(end).getValue() > pivotVal) {
            swap(list, start, end);
        }
        
        if (list.get(start).getValue() >= pivotVal) start++;
        if (list.get(end).getValue() <= pivotVal) end--;
    }
    
    swap(list, left, end);
    
    return end;
  }
  
  private void swap(List<Map.Entry<Integer, Integer>> list, int i, int j) {
    Map.Entry<Integer, Integer> entry = list.get(i);
    list.set(i, list.get(j));
    list.set(j, entry);
  }
}
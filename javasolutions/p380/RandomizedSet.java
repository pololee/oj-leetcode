/**
 * https://leetcode.com/problems/insert-delete-getrandom-o1/#/description
 *
 *
 */

package javasolutions.p380;

import java.util.HashMap;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class RandomizedSet {
  private HashMap<Integer, Integer> map;
  private List<Integer> nums;
  private Random rand;

  public RandomizedSet() {
    map = new HashMap<>();
    nums = new ArrayList<>();
    rand = new Random();
  }

  public boolean insert(int val) {
    if (map.containsKey(val)) return false;

    nums.add(val);
    map.put(val, nums.size() - 1 );
    return true;
  }

  public boolean remove(int val) {
    if (!map.containsKey(val)) return false;

    int lastVal = nums.get(nums.size() - 1 );
    int valIdx = map.get(val);

    nums.set(valIdx, lastVal);
    nums.remove(nums.size() - 1);
    map.put(lastVal, valIdx);
    map.remove(val);

    return true;
  }

  public int getRandom() {
    int idx = rand.nextInt(nums.size());

    return nums.get(idx);
  }
}
/**
 * https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/#/description
 
 */

package javasolutions.p381;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.Random;
import java.util.Collections;

public class RandomizedCollection {
  private ArrayList<Integer> nums;
  private HashMap<Integer, PriorityQueue<Integer>> locationsMap;
  private Random rand;

  public RandomizedCollection() {
    nums = new ArrayList<>();
    locationsMap = new HashMap<>();
    rand = new Random();
  }

  public boolean insert(int val) {
    boolean contained = locationsMap.containsKey(val);

    if(!contained) locationsMap.put(val, new PriorityQueue<Integer>(10, Collections.reverseOrder()));

    nums.add(val);
    locationsMap.get(val).add(nums.size() - 1);
    
    return !contained;
  }

  public boolean remove(int val) {
    if(!locationsMap.containsKey(val) || locationsMap.get(val).isEmpty()) return false;

    PriorityQueue<Integer> locations = locationsMap.get(val);
    int location = locations.poll(); // remove and return the right-most postion of val

    int length = nums.size();

    if(location < length - 1) {
      int lastVal = nums.get(length - 1);
      nums.set(location, lastVal);

      PriorityQueue<Integer> lastValLocations = locationsMap.get(lastVal);
      lastValLocations.remove(length - 1);
      lastValLocations.add(location);
    }

    nums.remove(length - 1);

    return true;
  }

  public int getRandom() {
    if(nums.isEmpty()) return Integer.MIN_VALUE;
    
    int random = rand.nextInt(nums.size());

    return nums.get(random);
  }

  public static void main(String[] args) {
    RandomizedCollection cal = new RandomizedCollection();

    cal.insert(10);
    cal.insert(10);
    cal.insert(20);
    cal.insert(20);
    cal.insert(30);
    cal.insert(30);

    cal.remove(10);
    cal.remove(10);
    cal.remove(30);
    cal.remove(30);
  }
}
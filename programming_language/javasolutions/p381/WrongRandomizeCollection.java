package javasolutions.p381;

import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;

public class WrongRandomizeCollection {
  ArrayList<Integer> nums;
  HashMap<Integer, List<Integer>> locs;
  Random rand;

  public WrongRandomizeCollection() {
    nums = new ArrayList<Integer>();
    locs = new HashMap<Integer, List<Integer>>();
    rand = new Random();
  }

  public boolean insert(int val) {
    System.out.println("Insert:  ");
    boolean contained = locs.containsKey(val);
    if( !contained ) {
      locs.put(val, new ArrayList<Integer>());
    }

    nums.add(val);
    locs.get(val).add(nums.size() - 1);

    System.out.println(nums.toString());

    return !contained;
  }

  public boolean remove(int val) {
    if(!locs.containsKey(val)) return false;

    System.out.println("Remove: ");

    List<Integer> locationList = locs.get(val);
    int location = locationList.remove( locationList.size() - 1 );

    if (location < nums.size() - 1 ) {
      int lastVal = nums.get( nums.size() - 1);
      nums.set(location, lastVal);

      List<Integer> lastValLocationList = locs.get(lastVal);
      lastValLocationList.remove( lastValLocationList.size() - 1 );
      lastValLocationList.add(location);
    }

    nums.remove( nums.size() - 1 );
    if(locs.get(val).isEmpty()) locs.remove(val);

    System.out.println(nums.toString());
    return true;
  }

  public static void main(String[] args) {
    WrongRandomizeCollection cal = new WrongRandomizeCollection();
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
    /**
     * The output
     * Insert:
     * [10]
     * Insert:
     * [10, 10]
     * Insert:
     * [10, 10, 20]
     * Insert:
     * [10, 10, 20, 20]
     * Insert:
     * [10, 10, 20, 20, 30]
     * Insert:
     * [10, 10, 20, 20, 30, 30]
     * Remove:
     * [10, 30, 20, 20, 30]
     * Remove:
     * [30, 30, 20, 20]
     * Remove:
     * [20, 30, 20]
     * Remove:
     * [20, 30]
     *
     * There should be no 30 in the last output.
     */
  }
 }
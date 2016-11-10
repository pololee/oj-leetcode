/*
  Assume there is no duplicates in the input arry.
*/

import java.util.HashMap;
import java.util.Arrays;

public class TwoSum {
  public static int[] findTwoSum(int[] arry, int sum) {
    HashMap<Integer, Integer> hmap = new HashMap<Integer, Integer>();
    int[] result = new int[2];

    for(int i = 0; i < arry.length; i++) {
      int x = arry[i];
      if(hmap.containsKey(sum - x)){
        result[0] = hmap.get(sum - x) + 1;
        result[1] = i + 1;
        return result;
      } else {
        hmap.put(x, i);
      }
    }

    throw new IllegalArgumentException("No two sum solution.");
  }

  public static void main(String[] args) {
    int[] test = {5, 2, 1, 3};
    int sum = 5;

    System.out.println(Arrays.toString(TwoSum.findTwoSum(test, sum)));
  }
}

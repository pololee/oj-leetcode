/**
https://leetcode.com/problems/russian-doll-envelopes/#/description

It's similar to p300 longest increasing sequence

Lambda expressions and Comparator
http://winterbe.com/posts/2014/03/16/java-8-tutorial/
 */

package javasolutions.p354;
import java.util.Arrays;

public class RussianDoll {
  public int maxEnvelopes(int[][] envelopes) {
    if(envelopes == null || envelopes.length == 0 || envelopes[0].length == 0) return 0;

    /**
    [width, height]
    Since the width is increasing, we only need to consider height.
[3, 4] cannot contains [3, 3], so we need to put [3, 4] before [3, 3] when sorting 
otherwise it will be counted as an increasing number if the order is [3, 3], [3, 4] 
*/
    Arrays.sort(envelopes, (int[] a, int[] b) -> {
      if(a[0] == b[0]) {
        return b[1] - a[1];
      } else {
        return a[0] - b[0];
      }
    });

    // Now we just need to find the length of longest increasing sequence in heights
    // Note not non-decreasing

    int[] tails = new int[envelopes.length];
    tails[0] = envelopes[0][1];
    int size = 1;

    for(int i = 1; i < envelopes.length; i++) {
      int height = envelopes[i][1];

      if(height < tails[0]) {
        tails[0] = height;
      } else if(height > tails[size - 1]) {
        tails[size] = height;
        size++;
      } else {
        int position = binarySearch(tails, 0, size - 1, height);
        tails[position] = height;
      }
    }

    return size;
  }

  private int binarySearch(int[] tails, int left, int right, int target) {
    while(left <= right) {
      int middle = left + (right - left) / 2;

      if(tails[middle] == target) {
        return middle;
      } else if (tails[middle] < target) {
        left = middle + 1;
      } else {
        right = middle - 1;
      }
    }

    return left;
  }

  public static void main(String[] args) {
    int[][] test = {
      {5, 4}, {6, 4}, {6, 7}, {2, 3}
    };

    RussianDoll cal = new RussianDoll();
    System.out.println(cal.maxEnvelopes(test));
  }
}
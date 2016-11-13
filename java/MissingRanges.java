/*
Note:
1. in the question, return value is a list of strings
2. If range is [start, end], add two "artificial" elements, start - 1, end + 1

 */

import java.util.List;
import java.util.ArrayList;

public class MissingRanges {
  public List<String> findMissingRanges(int[] array, int startRange, int endRange) {
    List<String> ranges = new ArrayList<String>();

    int prev = startRange - 1;
    for (int i = 0; i <= array.length; i++) {
      int current = (i == array.length) ? endRange + 1 : array[i];

      if (current - prev > 1) {
        ranges.add(getRange(prev + 1, current - 1));
      }
      prev = current;
    }

    return ranges;
  }

  private String getRange(int from, int to) {
    return (from == to) ? String.valueOf(from) : String.format("%d->%d", from, to);
  }

  public static void main(String[] args) {
    MissingRanges finder = new MissingRanges();
    int[] test1 = {0, 1, 3, 50, 75};

    List<String> ranges = finder.findMissingRanges(test1, 0, 100);
    for(String range : ranges) {
      System.out.println(range);
    }

    ranges = finder.findMissingRanges(new int[0], 0, 100);
    for(String range : ranges) {
      System.out.println(range);
    }
  }
}

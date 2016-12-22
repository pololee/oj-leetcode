package javasolutions.p163;

import java.util.ArrayList;
import java.util.List;

public class MissingRanges {
  public List<String> findRanges(int[] sortedArray, int begin, int end) {
    List<String> output = new ArrayList<>();

    int previous = begin - 1, current = 0, length = sortedArray.length;
    for(int i=0; i<=length; i++) {
      current = i == length ? end + 1 : sortedArray[i];

      if(current - previous > 1) {
        output.add(convertRange(previous + 1, current - 1));
      }

      previous = current;
    }

    return output;
  }

  private String convertRange(int rangeStart, int rangeEnd) {
    return rangeStart == rangeEnd ? String.valueOf(rangeStart) : String.format("%d->%d", rangeStart, rangeEnd);
  }

  public static void main(String[] args) {
    int[] test = {0, 1, 3, 50, 75};
    MissingRanges cal = new MissingRanges();
    List<String> result = cal.findRanges(test, 0, 99);

    for(String str : result) {
      System.out.println(str);
    }
  }
}
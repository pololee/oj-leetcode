package javasolutions.p401;

import java.util.List;
import java.util.ArrayList;

public class BinaryWatch {
  public List<String> readBinaryWatch(int num) {
    List<String> results = new ArrayList<>();

    int[] hourBaseList = { 8, 4, 2, 1};
    int[] minBaseList = { 32, 16, 8, 4, 2, 1 };

    for (int i = 0; i <= num; i++) {
      List<Integer> hourList = generateNumList(hourBaseList, i);
      List<Integer> minList = generateNumList(minBaseList, num - i);

      for (int hour : hourList) {
        if (hour > 11) continue;

        for (int min : minList) {
          if (min > 59) continue;
          results.add(String.format("%d:%02d", hour, min));
        }
      }
    }

    return results;
  }

  private List<Integer> generateNumList(int[] baseList, int count) {
    List<Integer> numList = new ArrayList<>();
    generateNumListHelper(baseList, 0, count, 0, numList);

    return numList;
  }

  private void generateNumListHelper(int[] baseList, int position, int count, int sum, List<Integer> numList) {
    if (count == 0) {
      numList.add(sum);
      return;
    }

    for (int i = position; i < baseList.length; i++) {
      generateNumListHelper(baseList, i + 1, count - 1, sum + baseList[i], numList);
    }
  }
}
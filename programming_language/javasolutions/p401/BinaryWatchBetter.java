package javasolutions.p401;

import java.util.List;
import java.util.ArrayList;

public class BinaryWatchBetter {
  public List<String> readBinaryWatch(int num) {
    List<String> results = new ArrayList<>();

    for (int hour = 0; hour < 12; hour++) {
      for (int min = 0; min < 60; min++) {
        if (Integer.bitCount( (hour << 6) + min ) == num) {
          results.add(String.format("%d:%02d", hour, min));
        }
      }
    }

    return results;
  }
}
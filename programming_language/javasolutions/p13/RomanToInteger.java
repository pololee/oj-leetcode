package javasolutions.p13;

import java.util.Map;
import java.util.HashMap;

public class RomanToInteger {

  private static final Map<Character, Integer> map = new HashMap<Character, Integer>() {{
    put('I', 1);
    put('V', 5);
    put('X', 10);
    put('L', 50);
    put('C', 100);
    put('D', 500);
    put('M', 1000);
  }};

  public int romanToInt(String s) {
    int prev = 0, total = 0;

    for (char ch : s.toCharArray()) {
      int current = map.get(ch);

      if (current > prev) {
        total += current - 2 * prev;
      } else {
        total += current;
      }

      prev = current;
    }

    return total;
  }
}
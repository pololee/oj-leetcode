// Use hashtable
// Assume only ASCII chars

import java.util.Arrays;

public class LongestSubstringWithoutRepeat {
  public int lengthOfLongestSubstring (String str) {
    int[] table = new int[256];
    Arrays.fill(table, -1);

    int maxLength = 0;
    int start = 0;
    for (int i = 0; i < str.length(); i++) {
      int numericValue = (int) str.charAt(i);
      if (table[numericValue] >= start) {
        start = table[numericValue] + 1;
      }

      table[numericValue] = i;
      maxLength = Math.max(maxLength, i - start + 1);
    }

    return maxLength;
  }

  public static void main(String[] args) {
    LongestSubstringWithoutRepeat soluton = new LongestSubstringWithoutRepeat();

    String test1 = "abcabcbb";
    String test2 = "bbbbbbb";

    System.out.println(test1);
    System.out.println(soluton.lengthOfLongestSubstring(test1));
    System.out.println(test2);
    System.out.println(soluton.lengthOfLongestSubstring(test2));
  }
}

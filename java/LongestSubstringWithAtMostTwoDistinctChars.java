// Use hashtable
// this question can be generalized to at most K distinct chars

import java.util.HashMap;
import java.util.Collections;
import java.util.Map;

public class LongestSubstringWithAtMostTwoDistinctChars {
  public int lengthOfLongestSubstring1 (String str, int k) {
    HashMap<Character, Integer> charMap = new HashMap<Character, Integer>();

    int start = 0;
    int maxLen = 0;
    for (int i = 0; i < str.length(); i++) {
      charMap.put(str.charAt(i), i);

      if (charMap.size() > k) {
        int value = Collections.min(charMap.values());
        start = value + 1;
        char key = findTheKey(charMap, value);
        charMap.remove(key);
      }

      maxLen = Math.max(maxLen, i - start + 1);
    }

    return maxLen;
  }

  public int lengthOfLongestSubstring2(String str, int k) {
    int[] count = new int[256];
    int numOfDistincts = 0, maxLen = 0, start = 0;

    for (int i = 0; i < str.length(); i++) {
      if (count[str.charAt(i)] == 0) {
        numOfDistincts++;
      }
      count[str.charAt(i)]++;

      while (numOfDistincts > k) {
        count[str.charAt(start)]--;
        if (count[str.charAt(start)] == 0) {
          numOfDistincts--;
        }
        start++;
      }

      maxLen = Math.max(maxLen, i - start + 1);
    }

    return maxLen;
  }

  private char findTheKey(HashMap<Character, Integer> charMap, int value) {
    for (Map.Entry entry : charMap.entrySet()) {
      if ((int)entry.getValue() == value) {
        return (char)entry.getKey();
      }
    }
    throw new IllegalArgumentException("Cannot find the key");
  }

  public static void main(String[] args) {
    LongestSubstringWithAtMostTwoDistinctChars solution = new LongestSubstringWithAtMostTwoDistinctChars();

    String test = "eceba";
    System.out.println(solution.lengthOfLongestSubstring1(test, 2));
    System.out.println(solution.lengthOfLongestSubstring2(test, 2));
  }
}

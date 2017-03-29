package javasolutions.p345;

import java.util.Set;
import java.util.HashSet;

public class ReverseVowels {
  private static final char[] VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};

  public String reverseVowels(String s) {
    if(s == null || s.isEmpty()) return null;

    StringBuilder builder = new StringBuilder(s);
    int left = 0, right = s.length() - 1;

    while(left <= right) {
      while(left < s.length() && !isVowel(s.charAt(left))) {
        left++;
      }

      while(right >= 0 && !isVowel(s.charAt(right))) {
        right--;
      }

      if(left >= right) {
        break;
      } else {
        char temp = s.charAt(left);
        builder.setCharAt(left, s.charAt(right));
        builder.setCharAt(right, temp);

        left++;
        right--;
      }
    }

    return builder.toString();
  }

  private boolean isVowel(char ch) {
    for(char c : VOWELS) {
      if(ch == c) return true;
    }

    return false;
  }

  public static void main(String[] args) {
    ReverseVowels cal = new ReverseVowels();

    System.out.println(cal.reverseVowels("hello"));
    System.out.println(cal.reverseVowels("leetcode"));
  }
}
package javasolutions.p389;

public class FindTheDifference {
  public char findTheDiff(String s, String t) {
    if(s.length() + 1 != t.length()) return '\0';

    int[] charMap = new int[26];

    for (char ch : s.toCharArray()) {
      charMap[ch - 'a']++;
    }

    for (char ch : t.toCharArray()) {
      int idx = ch - 'a';
      charMap[idx]--;

      if(charMap[idx] < 0) return ch;
    }

    return '\0';
  }

  public static void main(String[] args) {
    FindTheDifference cal = new FindTheDifference();
    System.out.println(cal.findTheDiff("abcd", "abcde"));
  }
}
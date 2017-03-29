/**
 * https://leetcode.com/problems/remove-duplicate-letters/?tab=Description
 */

package javasolutions.p316;


public class RemoveDupLetters {
  public String removeDuplicateLetters(String s) {
    int[] map = new int[26];
    boolean[] visited = new boolean[26];

    StringBuilder sb = new StringBuilder();
    sb.append('0');

    // fill in the frequency hash map
    for (char ch : s.toCharArray()) {
      map[ch - 'a']++;
    }

    for (char ch : s.toCharArray()) {
      map[ch  - 'a']--;
      if (visited[ch - 'a']) continue;

      char lastChar = sb.charAt( sb.length() - 1 );
      while (lastChar > ch && map[lastChar - 'a'] > 0) {
        visited[lastChar - 'a'] = false;

        sb.deleteCharAt( sb.length() - 1 );
        lastChar = sb.charAt( sb.length() - 1 );
      }

      sb.append(ch);
      visited[ ch - 'a' ] = true;
    }

    return sb.substring(1, sb.length());
  }

  public static void main(String[] args) {
    RemoveDupLetters cal = new RemoveDupLetters();

    System.out.println(cal.removeDuplicateLetters("bcabc"));
    System.out.println(cal.removeDuplicateLetters("cbacdcbc"));
  }
}

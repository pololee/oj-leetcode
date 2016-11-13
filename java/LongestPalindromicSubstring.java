public class LongestPalindromicSubstring {
  // We observe that a palindrome mirrors around its center.
  // Therefore, a palindrome can be expanded from its center,
  // and there are only 2n – 1 such centers.
  // You might be asking why there are 2n – 1 but not n centers?
  // The reason is the center of a palindrome can be in between two letters.
  // Such palindromes have even number of letters (such as “abba”) and
  // its center are between the two ‘b’s.
  // Since expanding a palindrome around its center could take O(n) time,
  // the overall complexity is O(n2).
  //
  public String expandFromCenter(String str) {
    if (str.isEmpty()) {
      return null;
    }

    if (str.length() == 1) {
      return str;
    }

    String longestSub = "", tempSub = "";

    for (int i = 0; i < str.length(); i++) {
      tempSub = search(str, i, i);
      if (tempSub.length() > longestSub.length()) {
        longestSub = tempSub;
      }

      tempSub = search(str, i, i + 1);
      if (tempSub.length() > longestSub.length()) {
        longestSub = tempSub;
      }
    }

    return longestSub;
  }

  private String search(String str, int leftCenter, int rightCenter) {
    int left = leftCenter, right = rightCenter;

    while (left >= 0 && right < str.length() && str.charAt(left) == str.charAt(right)) {
      left--;
      right++;
    }

    return str.substring(left + 1, right);
  }

  public static void main(String[] args) {
    LongestPalindromicSubstring finder = new LongestPalindromicSubstring();

    System.out.println(finder.expandFromCenter("abacdfgdcaba"));
  }
}

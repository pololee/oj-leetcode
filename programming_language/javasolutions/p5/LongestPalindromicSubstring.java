package javasolutions.p5;

public class LongestPalindromicSubstring {
  public String longestPalindrome(String s) {
    if(s.length() == 0) return null;

    if(s.length() == 1) return s;

    String longestSub = "", tempLongestSub = "", leftRightSameSub="", leftRightDiffSub="";
    for(int i=0; i<s.length(); i++) {
      leftRightSameSub = expand(s, i, i);

      if(i+1 < s.length() && s.charAt(i) == s.charAt(i+1)) {
        leftRightDiffSub = expand(s, i, i+1);
      }

      if(leftRightSameSub.length() > leftRightDiffSub.length()) {
        tempLongestSub = leftRightSameSub;
      } else {
        tempLongestSub = leftRightDiffSub;
      }

      if(tempLongestSub.length() > longestSub.length()) {
        longestSub = tempLongestSub;
      }
    }

    return longestSub;
  }

  private String expand(String original, int left, int right) {
    int subStart = left, subEnd = right;

    while(left >= 0 && right < original.length()) {
      if(original.charAt(left) == original.charAt(right)) {
        subStart = left;
        subEnd = right;
        left--;
        right++;
      } else {
        break;
      }
    }

    return original.substring(subStart, subEnd + 1);
  }

  public String longestPalindromeBetter(String s) {
    if(s.length() == 0) return null;

    if(s.length() == 1) return s;

    String longestSub = "", tempSub = "";
    for(int i=0; i<s.length(); i++) {
      tempSub = expandBetter(s, i, i);
      if(tempSub.length() > longestSub.length()) {
        longestSub = tempSub;
      }

      tempSub = expandBetter(s, i, i+1);
      if(tempSub.length() > longestSub.length()) {
        longestSub = tempSub;
      }
    }

    return longestSub;
  }

  private String expandBetter(String original, int left, int right) {
    while(left >= 0 && right < original.length() && original.charAt(left) == original.charAt(right)) {
      left--;
      right++;
    }

    // in any case when the loop stops, we always drop left and right position to get the substring
    return original.substring(left+1, right);
  }

  public static void main(String[] args) {
    String test = "babad";

    LongestPalindromicSubstring cal = new LongestPalindromicSubstring();
    System.out.println(cal.longestPalindromeBetter(test));
  }
}
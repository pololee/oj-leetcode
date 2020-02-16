package javasolutions.p409;

public class LongestPalindrome {
  public int longestPalindrome(String s) {
    if(s.isEmpty()) return 0;

    int[] countMap = new int[256];
    for(char ch : s.toCharArray()) {
      int index = ch - 'A';
      countMap[index]++;
    }

    int maxLength = 0;
    boolean pickOddNumLetter = false;

    for (int i=0; i<256; i++) {
      maxLength += countMap[i];

      if(countMap[i] % 2 == 1) {
        maxLength -= 1;
        pickOddNumLetter = true;
      }
    }

    return pickOddNumLetter ? maxLength + 1 : maxLength;
  }
}
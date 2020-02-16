package javasolutions.p159;

public class LongestSubstringWithAtMostTwoDistinct {
  public int lengthOfLongestSubstring(String s) {
    if(s.length() == 0) return 0;

    int[] map = new int[256];
    int counter = 0;

    int start = 0, length = s.length(), maxSubLength = 1;
    for(int i = 0; i < length; i++) {
      int asciiValue = (int) s.charAt(i);

      if(map[asciiValue] == 0) counter++;
      map[asciiValue]++;

      while(counter > 2) {
        int value = (int) s.charAt(start);
        map[value]--;
        start++;
        if(map[value] == 0) counter--;
      }

      maxSubLength = Math.max(maxSubLength, i - start + 1);
    }

    return maxSubLength;
  }

  public static void main(String[] args) {
    LongestSubstringWithAtMostTwoDistinct cal = new LongestSubstringWithAtMostTwoDistinct();

    System.out.println(cal.lengthOfLongestSubstring("eceba"));
  }
}
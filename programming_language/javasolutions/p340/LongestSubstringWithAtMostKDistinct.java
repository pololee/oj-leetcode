package javasolutions.p340;

public class LongestSubstringWithAtMostKDistinct {
  public int lengthOfSubstring(String s, int k) {
    if(s.length() == 0) return 0;

    int[] map = new int[256];
    int start = 0, counter = 0, length = s.length(), maxSubLength = 0;

    for(int i=0; i<length; i++) {
      int asciiValue = (int) s.charAt(i);

      if(map[asciiValue] == 0) counter++;
      map[asciiValue]++;

      while(counter > k) {
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
    LongestSubstringWithAtMostKDistinct cal = new LongestSubstringWithAtMostKDistinct();

    System.out.println(cal.lengthOfSubstring("eceba", 3));
  }
}
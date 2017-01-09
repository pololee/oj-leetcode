package javasolutions.p3;

public class LongestSubstringWithoutRepeat {
  public int lengthOfLongestSubstring(String s) {
    if(s.length() == 0) return 0;

    int start = 0, length = s.length(), maxSubLength = 0;
    int[] map = new int[256];
    for(int i=0; i<256; i++) {
      map[i] = -1;
    }

    for(int i=0; i<length; i++) {
      int asciiValue = (int) s.charAt(i);

      if(map[asciiValue] >= start) {
        start = map[asciiValue] + 1;
      }

      map[asciiValue] = i;
      maxSubLength = Math.max(maxSubLength, i - start + 1);
    }

    return maxSubLength;
  }

  public static void main(String[] args) {
    LongestSubstringWithoutRepeat cal = new LongestSubstringWithoutRepeat();
    System.out.println(cal.lengthOfLongestSubstring("abcabcbb"));
    System.out.println(cal.lengthOfLongestSubstring("bbbbb"));
    System.out.println(cal.lengthOfLongestSubstring("pwwkew"));
    System.out.println(cal.lengthOfLongestSubstring("pw"));
  }
}
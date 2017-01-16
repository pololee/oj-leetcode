package javasolutions.p28;

public class StrStr {
  public int strStr(String haystack, String needle){
    if(needle.length() == 0) return 0;
    if(needle.length() > haystack.length()) return -1;

    int haystackLength = haystack.length();
    int needleLength = needle.length();

    for (int start=0; start<haystackLength; start++) {
      for (int j=0; j<=needleLength; j++) {
        if (j == needleLength) {
          return start;
        }

        if((start + j) == haystackLength) {
          return -1;
        }

        if (haystack.charAt(start+j) != needle.charAt(j)) {
          break;
        }
      }
    }

    return -1;
  }
}
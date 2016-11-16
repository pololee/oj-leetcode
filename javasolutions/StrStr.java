public class StrStr {
  public int strstr(String needle, String haystack) {
    if (needle.isEmpty()) {
      return 0;
    }

    if (haystack.length() < needle.length()) {
      return -1;
    }

    for (int haystackIdx = 0; ; haystackIdx++) {
      for (int needleIdx = 0; ; needleIdx++) {
        if (needleIdx == needle.length()) {
          return haystackIdx;
        }

        if (haystackIdx + needleIdx == haystack.length()) {
          return -1;
        }

        if (needle.charAt(needleIdx) != haystack.charAt(haystackIdx + needleIdx)) {
          break;
        }
      }
    }
  }

  public static void main(String[] args) {
    StrStr finder = new StrStr();

    System.out.println(finder.strstr("ba", "aaaba"));
  }
}

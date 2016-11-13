public class OneEditDistance {
  public boolean isOneEditDistanceApart(String s, String t) {
    if (s.length() == t.length()) {
      return oneEditReplace(s, t);
    } else if (s.length() + 1 == t.length()) {
      return oneEditInsert(s, t);
    } else if (s.length() - 1 == t.length()) {
      return oneEditInsert(t, s);
    } else {
      return false;
    }
  }

  private boolean oneEditReplace(String s, String t) {
    if (s.length() != t.length()) {
      return false;
    }

    boolean foundDiff = false;
    for (int i = 0; i < s.length(); i++) {
      if (s.charAt(i) != t.charAt(i)) {
        if (foundDiff) {
          return false;
        }
        foundDiff = true;
      }
    }

    return true;
  }

  private boolean oneEditInsert(String shortStr, String longStr) {
    if (shortStr.length() + 1 != longStr.length()) {
      return false;
    }

    int i=0, j = 0;
    while (i < shortStr.length() && j < longStr.length()) {
      if (shortStr.charAt(i) != longStr.charAt(j)) {
        if (i != j) {
          return false;
        }
        j++;
      } else {
        i++;
        j++;
      }
    }

    return true;
  }

  public static void main(String[] args) {
    OneEditDistance checker = new OneEditDistance();

    System.out.println(checker.isOneEditDistanceApart("abcde", "abxde"));
    System.out.println(checker.isOneEditDistanceApart("abcde", "abcxde"));
    System.out.println(checker.isOneEditDistanceApart("abcde", "abcdex"));
    System.out.println(checker.isOneEditDistanceApart("abcde", "abcdexx"));
  }
}

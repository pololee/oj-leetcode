package javasolutions.p161;

public class OneEditDistance {
  public boolean isOneEditDistanceApart(String s, String t) {
    if(Math.abs(s.length() - t.length()) > 1) return false;

    if(s.length() == t.length()) {
      return replaceOne(s, t);
    } else if(s.length() > t.length()) {
      return addOne(t, s);
    } else {
      return addOne(s, t);
    }
  }

  private boolean replaceOne(String s, String t) {
    if(s.length() != t.length()) return false;

    int counter = 0;
    for(int i=0; i<s.length(); i++) {
      if(s.charAt(i) != t.charAt(i)) counter++;
    }

    return counter == 1;
  }

  private boolean addOne(String shortStr, String longStr) {
    if ( ( longStr.length() - shortStr.length() ) != 1 ) return false;

    int shortIdx = 0, longIdx = 0;
    boolean wasDiff = false;

    while(shortIdx < shortStr.length() && longIdx < longStr.length()) {
      if(shortStr.charAt(shortIdx) != longStr.charAt(longIdx) ) {
        if(wasDiff) {
          return false;
        } else {
          wasDiff = true;
          longIdx++;
        }
      } else {
        shortIdx++;
        longIdx++;
      }
    }

    return true;
  }

  public boolean isOneEditDistanceApartBetter(String s, String t) {
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
    OneEditDistance cal = new OneEditDistance();

    System.out.println(cal.isOneEditDistanceApart("abcde", "abXde"));
    System.out.println(cal.isOneEditDistanceApart("abcde", "abcXde"));
    System.out.println(cal.isOneEditDistanceApart("abcde", "abcdeX"));
    System.out.println(cal.isOneEditDistanceApart("abcde", "abcdeXXX"));
  }
}
package javasolutions.p397;

public class IntegerReplacement {
  public int intReplacement(int n) {
    return longReplacement((long)n);
  }

  private int longReplacement(long n) {
    if(n == 1) return 0;

    if( n % 2 == 0) {
      return 1 + longReplacement(n/2);
    } else {
      return 2 + Math.min(longReplacement((n+1)/2), longReplacement((n-1)/2));
    }
  }

  public int intReplacementIterative(int n) {
    if(n == 1) return 0;

    int count = 0;

    while(n != 1) {
      if(n % 2 == 0) {
        n /= 2;
      } else if (n == 3 || Long.bitCount((long) n+1) > Integer.bitCount(n-1)) {
        n--;
      } else {
        n++;
      }

      count++;
    }

    return count;
  }

  public int intReplacementIterativeBetter(int n) {
    if(n == 1) return 0;

    int count = 0;

    while(n != 1) {
      if(n % 2 == 0) {
        n /= 2;
      } else if (n == 3 || ((n >>> 1) & 1) == 0) {
        n--;
      } else {
        n++;
      }

      count++;
    }

    return count;
  }

  public static void main(String[] args) {
    IntegerReplacement cal = new IntegerReplacement();
    System.out.println(cal.intReplacement(8));
    System.out.println(cal.intReplacementIterative(6));
    System.out.println(cal.intReplacementIterativeBetter(6));
  }
}
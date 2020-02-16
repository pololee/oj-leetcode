/**
 * http://www.cnblogs.com/grandyang/p/5403783.html
 */

package javasolutions.p342;

// 1 1
// 4 100
// 16 10000
// 64 1000000
public class PowerOfFour {
  public boolean isPowerOfFour(int n) {
    return n > 0 && (n & (n-1)) == 0 && (n-1)%3 == 0;
  }

  public boolean isPowerOfFourAlso(int n) {
    return n > 0 && (n & (n-1)) == 0 && (n & 0x55555555) == n;
  }

  public boolean isPowerOfFourAlsoAgain(int n) {
    while(n > 0 && (n%4) == 0) {
      n /= 4;
    }

    return n == 1;
  }
}
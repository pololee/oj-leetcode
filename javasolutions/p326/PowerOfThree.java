package javasolutions.p326;

public class PowerOfThree {
  public boolean isPowerOfThree(int n) {
    while(n > 0 && n % 3 == 0) {
      n /= 3;
    }

    return n == 1;
  }

  // n is an integer, 0 ~ 2^31, so the maximum n that is power of 3 is 3^19 == 1162261467
  public boolean isPowerOfThreeAlso(int n) {
    return n > 0 && 1162261467 % n == 0;
  }

  
}
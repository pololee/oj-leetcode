package javasolutions.p70;

public class ClimbingStairs {
  public int climbStairs(int n) {
    if(n == 0) return 0;
    if(n == 1) return 1;
    if(n == 2) return 2;

    int a = 1, b = 2;
    for (int i = 3; i <= n; i++) {
      int temp = b + a;
      a = b;
      b = temp;
    }

    return b;
  }
}
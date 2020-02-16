/**
https://leetcode.com/problems/powx-n/#/description
 */

package javasolutions.p50;

public class Power {
  public double myPow(double x, int n) {
    if(n == 0) return 1;

    double half = myPow(x, n / 2);

    if(n % 2 == 0) {
      return half * half;
    } else if(n > 0) {
      return half * half * x;
    } else {
      return half * half / x;
    }
  }

  public double myPowIterative(double x, int n) {
    double answer = 1.0;

    for(int i = n; i != 0; i /= 2) {
      if(i % 2 != 0) answer *= x;
      x *= x;
    }

    return n > 0 ? answer : 1 / answer;
  }
}
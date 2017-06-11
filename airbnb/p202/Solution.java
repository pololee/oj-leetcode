/**
 * https://leetcode.com/problems/happy-number/#/description
 * Write an algorithm to determine if a number is "happy".
 * 
 * A happy number is a number defined by the following process: 
 * Starting with any positive integer, 
 * replace the number by the sum of the squares of its digits, 
 * and repeat the process until the number equals 1 (where it will stay), 
 * or it loops endlessly in a cycle which does not include 1. 
 * Those numbers for which this process ends in 1 are happy numbers
 *
 * Happy number wiki https://en.wikipedia.org/wiki/Happy_number
 */

package airbnb.p202;

import java.util.Set;
import java.util.HashSet;

public class Solution {
  public boolean isHappy(int n) {
    if(n <= 0) return false;

    Set<Integer> numSet = new HashSet<>();
    while(n > 1 && !numSet.contains(n)) {
      numSet.add(n);
      n = squareSum(n);
    }

    return n == 1;
  }

  public boolean isHappyPro(int n) {
    if(n <= 0) return false;

    while(n != 1 && n != 4) {
      n = squareSum(n);
    }

    return n == 1;
  }

  private int squareSum(int n) {
    if(n < 0) return 0;

    int result = 0;
    int remainder = 0;

    while(n > 0) {
      remainder = n % 10;
      result += remainder * remainder;
      n /= 10;
    }

    return result;
  }
}
/**
 * https://leetcode.com/problems/add-strings/#/description
 * Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
 * 
 * The length of both num1 and num2 is < 5100.
 * Both num1 and num2 contains only digits 0-9.
 * Both num1 and num2 does not contain any leading zero.
 * You must not use any built-in BigInteger library or convert the inputs to integer directly.
 */

package airbnb.p415;

public class Solution {
  public String addStrings(String num1, String num2) {
    if(num1 == null || num2 == null) return null;
    if(num1.length() == 0) return num2;
    if(num2.length() == 0) return num1;

    StringBuilder answer = new StringBuilder();
    int addOne = 0;
    int i = num1.length() - 1;
    int j = num2.length() - 1;

    while(i >= 0 && j >= 0) {
      int a = num1.charAt(i) - '0';
      int b = num2.charAt(j) - '0';

      int sum = a + b + addOne;
      answer.append(Integer.toString(sum % 10));
      addOne = sum / 10;

      i--;
      j--;
    }

    while(i >= 0) {
      int a = num1.charAt(i) - '0';
      int sum = a + addOne;

      answer.append(Integer.toString(sum % 10));
      addOne = sum / 10;

      i--;
    }

    while(j >= 0) {
      int b = num2.charAt(j) - '0';
      int sum = b + addOne;

      answer.append(Integer.toString(sum % 10));
      addOne = sum / 10;

      j--;
    }

    if(addOne > 0) {
      answer.append('1');
    }

    return answer.reverse().toString();
  }

  public static void main(String[] args) {
    String a = "99";
    String b = "1";
    Solution sol = new Solution();

    System.out.println(sol.addStrings(a, b));
  }
}

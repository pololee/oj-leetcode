/**
 * https://leetcode.com/problems/remove-k-digits/?tab=Solutions
 *
 * The whole idea of this method is to make small number move forward by at most k digits and output a number of length num.length-k.
 */

package javasolutions.p402;

public class RemoveKDigits {
  public String removeKdigits(String num, int k) {
    if (k == 0) return num;
    if (k == num.length()) return "0";

    int numToKeep = num.length() - k;
    char[] stack = new char[num.length()];
    int top = -1;

    for (int i = 0; i < num.length(); i++) {
      char ch = num.charAt(i);

      while (k > 0 && top >= 0 && stack[top] > ch) {
        top--;
        k--;
      }

      top++;
      stack[top] = ch;
    }

    // Find first non-zero char
    int index = 0;
    while(index < numToKeep && stack[index] == '0') index++;

    return index == numToKeep ? "0" : new String(stack, index, numToKeep - index);
  }

  public static void main(String[] args) {
    RemoveKDigits cal = new RemoveKDigits();

    System.out.println(cal.removeKdigits("1432219", 3));
    System.out.println(cal.removeKdigits("10200", 1));
    System.out.println(cal.removeKdigits("10", 2));
    System.out.println(cal.removeKdigits("11111111", 2));
  }
}
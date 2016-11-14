/**
 * Reverse digits of an integer. For example: x = 123, return 321.
 *
 * What about negative integers?
 * For input x = –123, you should return –321.
 *
 * What if the integer’s last digit is 0? For example, x = 10, 100, ...
 * Ignore the leading 0 digits of the reversed integer. 10 and 100 are both reversed as 1.
 *
 * What if the reversed integer overflows? For example, input x = 1000000003.
 * In this case, your function should return 0.
 */

public class ReverseInteger {
  private static final int maxDiv10 = Integer.MAX_VALUE / 10;

  public int reverse(int input) {
    if (input == 0) {
      return 0;
    }

    int output = 0;
    int temp = input;
    while (temp != 0) {
      if (output > maxDiv10 || output < (-1 * maxDiv10)) {
        return 0;
      }

      int digit = temp % 10;

      // if ret == 214748364, it must not overflow because the last reversed digit
      // is guaranteed to be 1 due to constraint of the input x.
      // if ((output == maxDiv10 && digit > 7) || (output == (-1 * maxDiv10) && digit > 8)) {
      //   return 0;
      // }

      output = output * 10 + digit;
      temp = temp / 10;
    }

    return output;
  }

  public static void main(String[] args) {
    ReverseInteger reverser = new ReverseInteger();

    System.out.println(reverser.reverse(123));
    System.out.println(reverser.reverse(-123));
    System.out.println(reverser.reverse(1000));
    System.out.println(reverser.reverse(1000000003));
  }
}

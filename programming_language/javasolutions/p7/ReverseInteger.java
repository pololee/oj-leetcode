package javasolutions.p7;

public class ReverseInteger {
  private static final int MAX_DIV_10 = Integer.MAX_VALUE / 10;

  public int reverse(int x) {
    if(x == Integer.MIN_VALUE) return 0;

    int sign = 0, original = 0;
    if(x >= 0) {
      sign = 1;
      original = x;
    } else {
      sign = -1;
      original = Math.abs(x);
    }

    int digit = 0, reversed = 0;
    while(original > 0) {
      digit = original % 10;

      if(reversed > MAX_DIV_10 || reversed == MAX_DIV_10 && digit >= 8) {
        return 0;
      }
      reversed = reversed * 10 + digit;

      original = original / 10;
    }

    return sign * reversed;
  }

  public int reverseBetter(int input) {
    if (input == 0) {
      return 0;
    }

    int output = 0;
    int temp = input;
    while (temp != 0) {
      if (output > MAX_DIV_10 || output < (-1 * MAX_DIV_10)) {
        return 0;
      }

      int digit = temp % 10;

      // if ret == 214748364, it must not overflow because the last reversed digit
      // is guaranteed to be 1 due to constraint of the input x.
      // if ((output == MAX_DIV_10 && digit > 7) || (output == (-1 * MAX_DIV_10) && digit > 8)) {
      //   return 0;
      // }

      output = output * 10 + digit;
      temp = temp / 10;
    }

    return output;
  }

  public static void main(String[] args) {
    ReverseInteger cal = new ReverseInteger();

    System.out.println(cal.reverse(123));
    System.out.println(cal.reverse(-123));
  }
}
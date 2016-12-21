package javasolutions.p8;

public class StringToInteger {
  private static final int MAX_DIV_TEN = Integer.MAX_VALUE / 10;

  public int myAtoi(String str) {
    if(str.length() == 0) return 0;

    int i = 0, length = str.length();
    while(i < length && Character.isWhitespace(str.charAt(i))) i++;

    int sign = 1;
    if(i < length && str.charAt(i) == '+') {
      i++;
    } else if(i < length && str.charAt(i) == '-') {
      sign = -1;
      i++;
    }

    int value = 0;
    while(i < length && Character.isDigit(str.charAt(i))) {
      int digit = Character.getNumericValue(str.charAt(i));
      
      if(value > MAX_DIV_TEN || (value == MAX_DIV_TEN && digit >= 8)) {
        return sign == -1 ? Integer.MIN_VALUE : Integer.MAX_VALUE;
      }

      value = value * 10 + digit;
      i++;
    }

    return sign * value;
  }
}
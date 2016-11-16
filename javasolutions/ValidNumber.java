/*
  1. Leading spaces - ignore
  2. Trailing spaces - ignore
  3. space between numbers - do not ignore
  4. additional chars after a number - not valid
  5. plus or minus sign - Valid
  6. cosider only numbers in decimal
  7. consider exponent
 */


public class ValidNumber {
  public static boolean isValidNumber (String str) {
    int i = 0, n = str.length();

    // skip leading space
    while (i < n && Character.isWhitespace(str.charAt(i))) i++;

    // sign + or -
    if (i < n && (str.charAt(i) == '+' || str.charAt(i) == '-')) {
      i++;
    }

    boolean valid = false;
    // Numbers before .
    while (i < n && Character.isDigit(str.charAt(i))) {
      i++;
      valid = true;
    }

    // . and numbers after .
    if (i < n && str.charAt == '.') {
      i++;
      while (i < n && Character.isDigit(str.charAt(i))) {
        i++;
        valid = true;
      }
    }

    // e and numbers after e
    if (valid && i < n && str.charAt(i) == 'e') {
      i++;
      valid = false;
      while ( i < n && Character.isDigit(str.charAt(i))) {
        i++;
        valid = true;
      }
    }

    // trailing spaces
    while (i < n && Character.isWhitespace(str.charAt(i))) i++;

    return valid && i = n;
  }
}

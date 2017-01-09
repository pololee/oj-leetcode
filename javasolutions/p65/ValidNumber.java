package javasolutions.p65;

public class ValidNumber {
  public boolean isNumber(String s) {
    if(s.length() == 0) return false;

    int i = 0, length = s.length();
    while(i < length && Character.isWhitespace(s.charAt(i))) i++;
    
    if(i < length && (s.charAt(i) == '+' || s.charAt(i) == '-')) i++;
    
    boolean isNumber = false;
    while(i < length && Character.isDigit(s.charAt(i))) {
      isNumber = true;
      i++;
    }

    // "1." is considered as a valid number
    if(i < length && s.charAt(i) == '.') {
      i++;

      while(i < length && Character.isDigit(s.charAt(i))) {
        isNumber = true;
        i++;
      }
    }

    if(isNumber && i < length && s.charAt(i) == 'e') {
      isNumber = false;
      i++;

      if(i < length && (s.charAt(i) == '+' || s.charAt(i) == '-')) i++;

      while(i < length && Character.isDigit(s.charAt(i))) {
        isNumber = true;
        i++;
      }
    }

    while(i < length && Character.isWhitespace(s.charAt(i))) i++;

    return i == length && isNumber;
  }

  public static void main(String[] args) {
    String test = " 005047e+6";
    ValidNumber cal = new ValidNumber();
    System.out.println(cal.isNumber(test));
  }
}
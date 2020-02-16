package javasolutions.p415;

public class AddStrings {
  public String addStrings(String num1, String num2) {
    int length1 = num1.length(), length2 = num2.length();
    int addOne = 0, sum = 0;
    StringBuilder builder = new StringBuilder();

    for(int i=length1-1, j=length2-1; i>=0 || j>=0; i--, j--) {
      int digit1 = i < 0 ? 0 : num1.charAt(i) - '0';
      int digit2 = j < 0 ? 0 : num2.charAt(j) - '0';

      sum = digit1 + digit2 + addOne;
      builder.append(sum % 10);
      addOne = sum / 10;
    }

    if(addOne > 0) {
      builder.append(1);
    }

    return builder.reverse().toString();
  }

  public static void main(String[] args) {
    String num1 = "99";
    String num2 = "110";

    AddStrings cal = new AddStrings();
    System.out.println(cal.addStrings(num1, num2));
  }
}
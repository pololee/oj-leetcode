public class ReverseWordsInString {
  public String reverse(String input) {
    int wordEndPlusOne = input.length() - 1;
    StringBuilder reversed = new StringBuilder();

    for (int i = input.length() - 1; i >= 0; i--) {
      if (Character.isWhitespace(input.charAt(i))) {
        wordEndPlusOne =  i;
      } else if (i == 0 || Character.isWhitespace(input.charAt(i - 1))) {
        if (reversed.length() > 0) {
          reversed.append(" ");
        }
        reversed.append(input.substring(i, wordEndPlusOne));
      }
    }

    return reversed.toString();
  }

  public static void main(String[] args) {
    String test = "the sky is blue";

    ReverseWordsInString reverser = new ReverseWordsInString();
    System.out.println(test);
    System.out.println(reverser.reverse(test));
  }
}

package javasolutions.p151;

public class ReverseWordsInAString {
  public String reverseWords(String s) {
    if(s.length() == 0) {
      return "";
    }

    int wordEnd = s.length();
    StringBuilder output = new StringBuilder();

    for(int i=s.length() - 1; i>=0; i--) {
      if(s.charAt(i) == ' ') {
        wordEnd = i;
      } else if(i==0 || s.charAt(i-1) == ' ') {
        if(output.length() != 0) output.append(' ');
        output.append(s.substring(i, wordEnd));
      }
    }

    return output.toString();
  }

  public static void main(String[] args) {
    String test = " 1";
    ReverseWordsInAString cal = new ReverseWordsInAString();
    System.out.println(cal.reverseWords(test));
  }
}
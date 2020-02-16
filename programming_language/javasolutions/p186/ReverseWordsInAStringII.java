package javasolutions.p186;

public class ReverseWordsInAStringII {
  public void reverseString(char[] charArray) {
    reverse(charArray, 0, charArray.length);

    for(int wordBegin=0, j=0; j<=charArray.length; j++) {
      if(j == charArray.length || charArray[j] == ' ') {
        reverse(charArray, wordBegin, j);
        wordBegin = j + 1;
      }
    }
  }

  private void reverse(char[] charArray, int begin, int endPlusOne) {
    for(int i=0; i < (endPlusOne - begin)/2; i++) {
      char temp = charArray[begin+i];
      charArray[begin+i] = charArray[endPlusOne-1-i];
      charArray[endPlusOne-1-i] = temp;
    }
  }

  public static void main(String[] args) {
    char[] test = "the sky is blue".toCharArray();
    ReverseWordsInAStringII cal = new ReverseWordsInAStringII();
    cal.reverseString(test);
    System.out.println(String.valueOf(test));
  }
}
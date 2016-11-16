/**
 * Key: think about matrix transpose properties
 * http://people.revoledu.com/kardi/tutorial/LinearAlgebra/MatrixTranspose.html
 */

// # Similar to Question [6. Reverse Words in a String], but with the following constraints:
// # “The input string does not contain leading or trailing spaces and the words
// # are always separated by a single space.”
// # Could you do it in-place without allocating extra space?
//
// # This is very important
// # a' = a
// # (ab)' = b'a'
// # we want ab -> ba
// # ab -> b'a'(by reverse the entire word) -> ba(by reverse each word)
// #

public class ReverseWordsInStringII {
  public void reverseWords(char[] input) {
    reverse(input, 0, input.length - 1);

    for (int i = 0, wordBegin = 0; i <= input.length; i++) {
      if (i == input.length || input[i] == ' ') {
        reverse(input, wordBegin, i - 1);
        wordBegin = i + 1;
      }
    }
  }

  private void reverse(char[] input, int beginIdx, int endIdx) {
    if (beginIdx > endIdx) {
      return;
    }
    for (int i = 0; i <= (endIdx - beginIdx)/2; i++) {
      if (beginIdx + i == endIdx - i) {
        break;
      }

      char temp = input[beginIdx + i];
      input[beginIdx + i] = input[endIdx - i];
      input[endIdx - i] = temp;
    }
  }

  public static void main(String[] args) {
    String str = "the sky is blue";
    char[] test = str.toCharArray();

    ReverseWordsInStringII reverser = new ReverseWordsInStringII();
    reverser.reverseWords(test);

    System.out.println(test);
  }
}

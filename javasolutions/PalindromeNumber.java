/**
 * Determine whether an integer is a palindrome. Do this without extra space.
 *
 * Does negative integer such as –1 qualify as a palindrome?
 * For the purpose of discussion here, we define negative integers as non-palindrome.
 */

public class PalindromeNumber {
  public boolean isPalindromic (int input) {
    if (input < 0) {
      return false;
    }

    int left = input;
    int right = 0;
    while (left > right) {
      right = right * 10 + left % 10;
      left = left / 10;

      if (left == right || (left / 10) == right) {
        return true;
      }
    }

    return false;
  }

  public static void main(String[] args) {
    PalindromeNumber checker = new PalindromeNumber();

    System.out.println(checker.isPalindromic(12321));
    System.out.println(checker.isPalindromic(123321));
    System.out.println(checker.isPalindromic(0));
    System.out.println(checker.isPalindromic(20));
    System.out.println(checker.isPalindromic(22));
  }
}

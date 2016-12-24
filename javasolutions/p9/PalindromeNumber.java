package javasolutions.p9;

public class PalindromeNumber {
  public boolean isPalindrome(int x) {
    if(x < 0) return false;

    int divider = 1;
    while(x / divider > 9) {
      divider *= 10;
    }

    int left = 0, right = 0;
    while(x != 0) {
      left = x / divider;
      right = x % 10;

      if(left != right) return false;

      x = (x % divider) / 10;
      divider /= 100;
    }

    return true;
  }

  public static void main(String[] args) {
    PalindromeNumber cal = new PalindromeNumber();
    System.out.println(cal.isPalindrome(123));
    System.out.println(cal.isPalindrome(12321));
    System.out.println(cal.isPalindrome(123321));
    System.out.println(cal.isPalindrome(1));
    System.out.println(cal.isPalindrome(10));
    System.out.println(cal.isPalindrome(11));
  }
}
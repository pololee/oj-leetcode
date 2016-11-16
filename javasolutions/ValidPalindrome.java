public class ValidPalindrome {
  public boolean isValidPalindrome(String str) {
    if (str.isEmpty()) {
      return true;
    }

    str = str.toLowerCase();

    int low = 0;
    int high = str.length() - 1;

    while (low < high) {
      while (low < high && isNotAphanumeric(str.charAt(low))) {
        low++;
      }

      while (low < high && isNotAphanumeric(str.charAt(high))) {
        high--;
      }

      if(str.charAt(low) != str.charAt(high)) {
        return false;
      }

      low++;
      high--;
    }

    return true;
  }

  private boolean isNotAphanumeric(char ch){
    return !Character.isLetterOrDigit(ch);
  }

  public static void main(String[] args) {
    ValidPalindrome checker = new ValidPalindrome();
    System.out.println(checker.isValidPalindrome("A man, a plan, a canal: Panama"));
    System.out.println(checker.isValidPalindrome("race a car"));
  }
}

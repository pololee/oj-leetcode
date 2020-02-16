package javasolutions.p17;

import java.util.List;
import java.util.HashMap;
import java.util.ArrayList;

public class LetterCombinations {
  private static final HashMap<Character, String> digitToLetters;

  static {
    digitToLetters = new HashMap<Character, String>();
    digitToLetters.put('1', "1");
    digitToLetters.put('2', "abc");
    digitToLetters.put('3', "def");
    digitToLetters.put('4', "ghi");
    digitToLetters.put('5', "jkl");
    digitToLetters.put('6', "mno");
    digitToLetters.put('7', "pqrs");
    digitToLetters.put('8', "tuv");
    digitToLetters.put('9', "wxyz");
    digitToLetters.put('0', "0");
  }

  public List<String> letterCombinations(String digits) {
    List<String> results = new ArrayList<>();
    StringBuilder oneResult = new StringBuilder();

    if (digits.isEmpty()) return results;

    letterCombinationsDFS(digits, 0, oneResult, results);
    return results;
  }

  private void letterCombinationsDFS(String digits, int level, StringBuilder oneResult, List<String> results) {
    if (level == digits.length()) {
      results.add(oneResult.toString());
      return;
    } else {
      String str = digitToLetters.get(digits.charAt(level));

      for (int i = 0; i < str.length(); i++) {
        oneResult.append(str.charAt(i));
        letterCombinationsDFS(digits, level + 1, oneResult, results);
        oneResult.deleteCharAt(oneResult.length() - 1);
      }
    }
  }
}
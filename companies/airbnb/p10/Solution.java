// # https://leetcode.com/problems/regular-expression-matching/description/

// # 10. Regular Expression Matching
// # Implement regular expression matching with support for '.' and '*'.

// # '.' Matches any single character.
// # '*' Matches zero or more of the preceding element.

// # The matching should cover the entire input string (not partial).

// # The function prototype should be:
// # bool isMatch(const char *s, const char *p)

// # Some examples:
// # isMatch("aa","a") → false
// # isMatch("aa","aa") → true
// # isMatch("aaa","aa") → false
// # isMatch("aa", "a*") → true
// # isMatch("aa", ".*") → true
// # isMatch("ab", ".*") → true
// # isMatch("aab", "c*a*b") → true

package airbnb.p10;

public class Solution {
  public boolean isMatch(String text, String pattern) {
    if (text == null || pattern == null) {
      return false;
    }

    int textLength = text.length();
    int patternLength = pattern.length();
    boolean[][] dpState = new boolean[textLength + 1][patternLength + 1];

    dpState[0][0] = true;

    for(int j = 1; j <= patternLength; j++) {
      if (pattern.charAt(j-1) == '*') {
        dpState[0][j] = dpState[0][j-2];
      }
    }

    for(int i = 1; i <= textLength; i++) {
      for(int j = 1; j <= patternLength; j++) {
        if (charIsMatch(text.charAt(i-1), pattern.charAt(j-1))) {
          dpState[i][j] = dpState[i-1][j-1];
        } else if(pattern.charAt(j-1) == '*') {
          if (charIsMatch(text.charAt(i-1), pattern.charAt(j-2))) {
            dpState[i][j] = dpState[i-1][j] || dpState[i][j-2];
          } else {
            dpState[i][j] = dpState[i][j-2];
          }
        }
      }
    }

    return dpState[textLength][patternLength];
  }

  private boolean charIsMatch(char textChar, char patternChar) {
    return textChar == patternChar || patternChar == '.';
  }
}
/**
 * https://leetcode.com/problems/valid-parentheses/#/description
 * Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
 * The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
 */

package airbnb.p20;

import java.util.Map;
import java.util.HashMap;
import java.util.Stack;

public class Solution {
  private static final Map<Character, Character> map;
  static {
    map = new HashMap<>();
    map.put('(', ')');
    map.put('[', ']');
    map.put('{', '}');
  }

  public boolean isValid(String s) {
    if(s.length() == 0) return true;

    Stack<Character> stack = new Stack<>();
    for(char ch : s.toCharArray()) {
      if(map.containsKey(ch)) {
        stack.push(ch);
      } else if(stack.isEmpty() || ch != map.get(stack.pop())) {
        return false;
      }
    }

    return stack.isEmpty();
  }
}

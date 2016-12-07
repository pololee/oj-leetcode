package javasolutions.p20;

import java.util.Map;
import java.util.HashMap;
import java.util.Stack;

public class ValidParentheses {
  private static final Map<Character, Character> map = new HashMap<Character, Character>() {{
    put('(', ')');
    put('{', '}');
    put('[', ']');
  }};

  public boolean isValid(String s) {
    Stack<Character> stack = new Stack<>();

    for(char ch : s.toCharArray()) {
      if (map.containsKey(ch)) {
        stack.push(ch);
      } else if (stack.isEmpty() || ch != map.get(stack.pop())) {
        return false;
      }
    }

    return stack.isEmpty();
  }
}
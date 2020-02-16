package javasolutions.p150;

import java.util.Map;
import java.util.HashMap;
import java.util.Stack;

public class BetterReversePolishNotation {
  private static final Map<String, Operator> OPERATORS = new HashMap<String, Operator>() {{
    put("+", new Operator() {
      public int eval(int x, int y) { return x + y; }
    });

    put("-", new Operator() {
      public int eval(int x, int y) { return x - y; }
    });

    put("*", new Operator() {
      public int eval(int x, int y) { return x * y; }
    });

    put("/", new Operator() {
      public int eval(int x, int y) { return x / y; }
    });
  }};

  public int evalRPN(String[] tokens) {
    Stack<Integer> stack = new Stack<>();

    for(String token : tokens) {
      if(OPERATORS.containsKey(token)) {
        int y = stack.pop();
        int x = stack.pop();
        stack.push(OPERATORS.get(token).eval(x, y));
      } else {
        stack.push(Integer.parseInt(token));
      }
    }

    return stack.pop();
  }

  public static void main(String[] args) {
    BetterReversePolishNotation rpn = new BetterReversePolishNotation();
    String[] test = {"2", "1", "+", "3", "*"};
    System.out.println(rpn.evalRPN(test));
  }
}
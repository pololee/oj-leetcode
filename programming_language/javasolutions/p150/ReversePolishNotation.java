package javasolutions.p150;

import java.util.Stack;

public class ReversePolishNotation {
  public int evalRPN(String[] tokens) {
    Stack<Integer> stack = new Stack<>();

    for(String token : tokens) {
      if(isOperator(token)) {
        int rightOperand = stack.pop();
        int leftOperand = stack.pop();
        stack.push(calculate(token, leftOperand, rightOperand));
      } else {
        stack.push(Integer.valueOf(token));
      }
    }

    return stack.pop();
  }

  private boolean isOperator(String token) {
    return token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/");
  }

  private int calculate(String operator, int leftOperand, int rightOperand) {
    switch (operator) {
      case "+": return leftOperand + rightOperand;
      case "-": return leftOperand - rightOperand;
      case "*": return leftOperand * rightOperand;
      case "/": return leftOperand / rightOperand;
      default: throw new IllegalArgumentException();
    }
  }

  public static void main(String[] args) {
    ReversePolishNotation rpn = new ReversePolishNotation();
    String[] test = {"2", "1", "+", "3", "*"};
    System.out.println(rpn.evalRPN(test));
  }
}
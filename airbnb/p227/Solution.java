package airbnb.p227;

import java.util.Stack;

public class Solution {
  public int calculate(String s) {
    int num = 0;
    Stack<Integer> stack = new Stack<>();
    char sign = '+';

    for(int i = 0; i < s.length(); i++) {
      char ch = s.charAt(i);
      if (Character.isDigit(ch)) {
        num = num * 10 + ch - '0';
      }

      if ((!Character.isDigit(ch) && ch != ' ') || i == s.length() - 1) {
        if (sign == '+') {
          stack.push(num);
        } else if(sign == '-') {
          stack.push(-1 * num);
        } else if(sign == '/') {
          int leftNumber = stack.pop();
          stack.push(leftNumber / num);
        } else if(sign == '*') {
          int leftNumber = stack.pop();
          stack.push(leftNumber * num);
        }

        num = 0;
        sign = ch;
      }
    }

    int answer = 0;
    while(!stack.isEmpty()) {
      int number = stack.pop();
      answer += number;
    }

    return answer;
  }
}
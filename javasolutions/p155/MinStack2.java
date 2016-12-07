package javasolutions.p155;

import java.util.Stack;

public class MinStack2 {
  private Stack<Integer> mainStack;
  private Stack<Integer> minStack;

  /** initialize your data structure here. */
  public MinStack2() {
      mainStack = new Stack<Integer>();
      minStack = new Stack<Integer>();
  }

  public void push(int x) {
      if(minStack.isEmpty()) {
          minStack.push(x);
      } else {
          minStack.push(Math.min(x, minStack.peek()));
      }

      mainStack.push(x);
  }

  public void pop() {
      minStack.pop();
      mainStack.pop();
  }

  public int top() {
      return mainStack.peek();
  }

  public int getMin() {
      return minStack.peek();
  }
}
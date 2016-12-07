package javasolutions.p155;

import java.util.Stack;

public class MinStack {
  private Stack<Integer> mainStack;
  private Stack<Integer> minimumStack;

  public MinStack() {
    mainStack = new Stack<Integer>();
    minimumStack = new Stack<Integer>();
  }

  public void push(int x) {
    mainStack.push(x);

    if (minimumStack.isEmpty() || x <= minimumStack.peek()) {
      minimumStack.push(x);
    }
  }

  public int pop() {
    int element = mainStack.pop();

    if (element == minimumStack.peek()) {
      minimumStack.pop();
    }

    return element;
  }

  public int top() {
    return mainStack.peek();
  }

  public int getMin() {
    return minimumStack.peek();
  }
}
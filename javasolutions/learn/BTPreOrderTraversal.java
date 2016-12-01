package javasolutions.learn;

import java.util.Stack;

public class BTPreOrderTraversal<T> {
  public void recursiveTraversal(BTNode<T> root) {
    String output = new String();
    output = recursiveHelper(root, output);
    System.out.println(output);
  }

  private String recursiveHelper(BTNode<T> root, String str) {
    if (root == null) {
      return "";
    } else {
      str = root.toString() + " ";
      str = str + recursiveHelper(root.left, str);
      str = str + recursiveHelper(root.right, str);
    }
    return str;
  }
/**
 * To convert an inherently recursive procedures to iterative, we need an explicit stack.
 *
 * 1.Create an empty stack nodeStack and push root node to stack.
 * 2.Do following while nodeStack is not empty.
 *   a.Pop an item from stack and print it.
 *   b.Push right child of popped item to stack
 *   c.Push left child of popped item to stack
 * Right child is pushed before left child to make sure that left subtree is processed first.
 * @param root [description]
 */

  public void iterativeTraversal(BTNode<T> root) {
    if (root == null) {
      return;
    }

    StringBuilder output = new StringBuilder();
    Stack<BTNode<T>> stack = new Stack<>();
    stack.push(root);

    BTNode<T> current = null;
    while(!stack.empty()) {
    	current = stack.pop();
    	output.append(current.toString()).append(" ");

    	if (current.right != null) {
    		stack.push(current.right);
    	}

    	if (current.left != null) {
    		stack.push(current.left);
    	}
    }
    output = output.deleteCharAt(output.length() - 1);
    System.out.println(output.toString());
  }

  public static void main(String[] args) {
    // http://stackoverflow.com/questions/24991/why-cant-i-explicitly-pass-the-type-argument-to-a-generic-java-method
    BTNode<String> root = BTNode.<String>dummyTree();
    BTPreOrderTraversal<String> travel = new BTPreOrderTraversal<>();
    travel.recursiveTraversal(root);
    travel.iterativeTraversal(root);
  }
}
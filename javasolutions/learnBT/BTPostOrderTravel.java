package javasolutions.learnBT;

import javasolutions.learnBT.TreeNode;
import java.util.Stack;

public class BTPostOrderTravel {
  public void recursive(TreeNode root) {
    if(root == null) return;

    String output = "";
    output = recursiveHelper(root, output);
    System.out.println(output);
  }

  private String recursiveHelper(TreeNode root, String output) {
    if(root == null) return "";

    output = recursiveHelper(root.left, output);
    output = output + recursiveHelper(root.right, output);
    output = output + String.valueOf(root.val) + "#";
    return output;
  }

  //     1
  //   2,   3
  // 4, 5  6, 7

  // Pre-order: 1 2 4 5 3 6 7
  // Post-order: 4 5 2 6 7 3 1
  // Pre-order right first: 1 3 7 6 2 5 4
  // So reverse of pre-order right first == post-order
  public void iterative(TreeNode root) {
    if(root == null) return;

    Stack<TreeNode> preOrderRightFirstStack = new Stack<>();
    Stack<TreeNode> postOrderStack = new Stack<>();
    preOrderRightFirstStack.push(root);

    while(!preOrderRightFirstStack.empty()) {
      TreeNode node = preOrderRightFirstStack.pop();
      postOrderStack.push(node);

      if(node.left != null) preOrderRightFirstStack.push(node.left);
      if(node.right != null) preOrderRightFirstStack.push(node.right);
    }

    StringBuilder builder = new StringBuilder();
    while(!postOrderStack.empty()) {
      TreeNode node = postOrderStack.pop();
      builder.append(String.valueOf(node.val)).append("#");
    }

    System.out.println(builder.toString());
  }

  public void iterativeOneStack(TreeNode root) {
    if(root == null) return;

    Stack<TreeNode> stack = new Stack<>();
    stack.push(root);
    TreeNode previous = null;
    StringBuilder builder = new StringBuilder();

    while(!stack.empty()) {
      TreeNode current = stack.peek();

      // case 1: moving down the tree
      if(previous == null || current == previous.left || current == previous.right) {
        if(current.left != null) {
          // if left is null, then move the left first
          stack.push(current.left);
        } else if(current.right != null) {
          stack.push(current.right);
        } else {
          stack.pop();
          builder.append(String.valueOf(current.val)).append("#");
        }
      }

      // case 2: moving up from the left subtree
      if(previous == current.left) {
        if(current.right != null) {
          stack.push(current.right);
        } else {
          stack.pop();
          builder.append(String.valueOf(current.val)).append("#");
        }
      }

      // case 3: moving up from the right subtree
      if(previous == current.right) {
        stack.pop();
        builder.append(String.valueOf(current.val)).append("#");
      }

      previous = current;
    }

    System.out.println(builder.toString());
  }

  public static void main(String[] args) {
    TreeNode root = TreeNode.dummyTree();

    BTPostOrderTravel travel = new BTPostOrderTravel();
    travel.recursive(root);
    travel.iterative(root);
    travel.iterativeOneStack(root);
  }
}
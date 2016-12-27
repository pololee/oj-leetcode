package javasolutions.learnBT;

import javasolutions.learnBT.TreeNode;
import java.util.Stack;

public class BTInOrderTravel {
  public void recursive(TreeNode root) {
    if(root == null) return;

    String output = "";
    output = recursiveHelper(root, output);
    System.out.println(output);
  }

  private String recursiveHelper(TreeNode root, String output) {
    if(root == null) return "";

    output = recursiveHelper(root.left, output);
    output = output + String.valueOf(root.val) + "#";
    output = output + recursiveHelper(root.right, output);
    return output;
  }

  public void iterative(TreeNode root) {
    if(root == null) return;

    Stack<TreeNode> stack = new Stack<>();
    StringBuilder builder = new StringBuilder();

    TreeNode node = root;
    while(node != null) {
      stack.push(node);
      node = node.left;
    }

    while(!stack.empty()) {
      TreeNode current = stack.pop();
      builder.append(String.valueOf(current.val)).append("#");

      if(current.right != null) {
        TreeNode tmp = current.right;
        while(tmp != null) {
          stack.push(tmp);
          tmp = tmp.left;
        }
      }
    }

    System.out.println(builder.toString());
  }

  public static void main(String[] args) {
    TreeNode root = TreeNode.dummyTree();

    BTInOrderTravel travel = new BTInOrderTravel();
    travel.recursive(root);
    travel.iterative(root);
  }
}
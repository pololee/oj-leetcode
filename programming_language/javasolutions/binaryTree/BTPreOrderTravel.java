package javasolutions.binaryTree;

import javasolutions.binaryTree.TreeNode;
import java.util.Stack;

public class BTPreOrderTravel {
  public void recursive(TreeNode root) {
    if(root == null) return;

    String output = "";
    output = recursiveHelper(root);
    System.out.println(output);
  }

  private String recursiveHelper(TreeNode root) {
    if(root == null) return "";

    String output = String.valueOf(root.val) + "#";
    output = output + recursiveHelper(root.left);
    output = output + recursiveHelper(root.right);
    return output;
  }

  public void iterative(TreeNode root) {
    if(root == null) return;

    StringBuilder builder = new StringBuilder();
    Stack<TreeNode> stack = new Stack<>();
    stack.push(root);

    while(!stack.empty()) {
      TreeNode node = stack.pop();
      builder.append(String.valueOf(node.val)).append("#");
      
      if(node.right != null) stack.push(node.right);
      if(node.left != null) stack.push(node.left);
    }

    System.out.println(builder.toString());
  }

  public static void main(String[] args) {
    TreeNode root = TreeNode.dummyTree();

    BTPreOrderTravel travel = new BTPreOrderTravel();
    travel.recursive(root);
    travel.iterative(root);
  }
}
package javasolutions.learnBT;

import javasolutions.learnBT.TreeNode;

public class BTInOrderSearch {
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

  public static void main(String[] args) {
    TreeNode root = TreeNode.dummyTree();

    BTInOrderSearch search = new BTInOrderSearch();
    search.recursive(root);
  }
}
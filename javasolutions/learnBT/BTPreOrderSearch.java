package javasolutions.learnBT;

import javasolutions.learnBT.TreeNode;

public class BTPreOrderSearch {
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

  public static void main(String[] args) {
    TreeNode root = TreeNode.dummyTree();

    BTPreOrderSearch search = new BTPreOrderSearch();
    search.recursive(root);
  }
}
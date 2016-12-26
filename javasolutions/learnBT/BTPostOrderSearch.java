package javasolutions.learnBT;

import javasolutions.learnBT.TreeNode;

public class BTPostOrderSearch {
  public void recursive(TreeNode root) {
    if(root == null) return;

    String output = "";
    output = recursiveHelper(root, output);
    System.out.println(output);
  }

  public String recursiveHelper(TreeNode root, String output) {
    if(root == null) return "";

    output = recursiveHelper(root.left, output);
    output = output + recursiveHelper(root.right, output);
    output = output + String.valueOf(root.val) + "#";
    return output;
  }

  public static void main(String[] args) {
    TreeNode root = TreeNode.dummyTree();

    BTPostOrderSearch search = new BTPostOrderSearch();
    search.recursive(root);
  }
}
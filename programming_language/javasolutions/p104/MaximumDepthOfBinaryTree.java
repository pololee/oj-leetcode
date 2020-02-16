package javasolutions.p104;

import javasolutions.TreeNode;

public class MaximumDepthOfBinaryTree {
  public int maxDepth(TreeNode root) {
    if (root == null) {
      return 0;
    } else {
      return Math.max(maxDepth(root.left) + 1, maxDepth(root.right) + 1);
    }
  }

  public static void main(String[] args) {
    TreeNode root = TreeNode.dummyTree();
    MaximumDepthOfBinaryTree cal = new MaximumDepthOfBinaryTree();
    int result = cal.maxDepth(root);
    System.out.println(result);
  }
}
package javasolutions.leetcodeBook;

import javasolutions.TreeNode;

public class BalancedBinaryTree {
  public boolean isBalanced(TreeNode root) {
    if(root == null) return true;

    return isBalancedHelper(root) != -1;
  }

  // user -1 to indicate the tree rooted at the input root is not a balance tree
  public int isBalancedHelper(TreeNode root) {
    if(root == null) return 0;

    int left = isBalancedHelper(root.left);
    if(left == -1) return -1;

    int right = isBalancedHelper(root.right);
    if(right == -1) return -1;

    if(Math.abs(left - right) > 1) {
      return -1;
    } else {
      return Math.max(left, right) + 1;
    }
  }
}
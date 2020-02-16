/**
 * https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/?tab=Description
 *
 * The lowest common ancestor is defined between two node v and w, as the lowest node in T that
 * has both v and w as descendants (where we allow a node to be a descendant of itself)
 */

package javasolutions.p236;

import javasolutions.TreeNode;

public class LowestCommonAncestor {
  public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    if (root == null || root == p || root == q) return root;

    TreeNode left = lowestCommonAncestor(root.left, p, q);
    if (left != null && left != p && left != q) return left;

    TreeNode right = lowestCommonAncestor(root.right, p, q);
    if(right != null && right != p && right != q) return right;

    if(left == null) {
      return right;
    } else if (right == null) {
      return left;
    } else {
      return root;
    }
  }
}
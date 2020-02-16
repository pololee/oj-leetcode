/**
 * https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/?tab=Description
 */

package javasolutions.p235;

import javasolutions.TreeNode;

public class LowestCommonAncestor {
  public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    if (root == null) return null;

    if (root.val > Math.max(p.val, q.val)) {
      return lowestCommonAncestor(root.left, p, q);
    } else if (root.val < Math.min(p.val, q.val)) {
      return lowestCommonAncestor(root.right, p, q);
    } else {
      return root;
    }
  }


  public TreeNode lowestCommonAncestorIterative(TreeNode root, TreeNode p, TreeNode q) {
    if (root == null) return null;

    TreeNode current = root;
    while(current != null) {
      if (current.val > Math.max(p.val, q.val)) {
        current = current.left;
      } else if (current.val < Math.min(p.val, q.val)) {
        current = current.right;
      } else {
        break;
      }
    }

    return current;
  }
}
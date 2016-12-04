/**
 * This is a stupid question, because you need to understand what it is really asking for?
 *
 * Here is an example:
 *
 * Original Tree
 *             1
 *       2          3
 *    4     5
 * After conversion:
 *            4
 *       5           2
 *               3      1
 *
 * So what actually happened? Bullshit
 *
 * Let's say current node is p, its parent is parent,
 * p.left = parent.right(which is its sibling)
 * p.right = parent
 */



package javasolutions.p156;

import javasolutions.TreeNode;

public class BTUpsideDown {
  /**
   * Top down approach
   * keep the record of parent and parentRight
   */
  public TreeNode upsideDown(TreeNode root) {
    TreeNode current = root, parent = null, parentRight = null;

    while (current != null) {
      TreeNode left = current.left;

      current.left = parentRight;
      parentRight = current.right;

      current.right = parent;
      parent = current;

      current = left;
    }

    return parent;
  }

  /**
   * Bottom up approach
   */
  public TreeNode upsideDownV2(TreeNode root) {
    return dfsUpsideDown(root, null);
  }

  private TreeNode dfsUpsideDown(TreeNode node, TreeNode parent) {
    if (node == null) {
      return parent;
    }

    TreeNode root = dfsUpsideDown(node.left, node);
    node.left = (parent == null) ? null : parent.right;
    node.right = parent;

    return root;
  }
}
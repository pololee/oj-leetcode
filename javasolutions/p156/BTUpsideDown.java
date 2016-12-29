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

  public TreeNode upsideDownRecursive(TreeNode root) {
    return upsideDownRecursiveHelper(root, null);
  }

  private TreeNode upsideDownRecursiveHelper(TreeNode node, TreeNode parent) {
    if(node == null) return parent;
    TreeNode root = upsideDownRecursiveHelper(node.left, node);

    if(parent == null) {
      node.left = null;
      node.right = null;
    } else {
      node.left = parent.right;
      node.right = parent;
    }

    return root;
  }
}
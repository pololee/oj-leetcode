package javasolutions.p98;

import javasolutions.TreeNode;
import java.util.Stack;

public class ValidateBinarySearchTree {
    /**
     * Top down search, need to keep the low end and high end
     * 
     *       10
     *   5          15
     *           6     20
     * As we traverse down the tree from node (10) to right node (15), 
     * we know for sure that the right node’s value fall between 10 and + . 
     * Then, as we traverse further down from node (15) to left node (6), 
     * we know for sure that the left node’s value fall between 10 and 15. 
     * And since (6) does not satisfy the above requirement, 
     * we can quickly determine it is not a valid BST.              
     */
    public boolean isValidBST(TreeNode root) {
      topDownSearchValid(root, null, null);
    }

    private boolean topDownSearchValid(TreeNode node, Integer low, Integer high) {
      if (node == null) {
        return true;
      } else {
        return (low == null || node.val > low) && (high == null || node.val < high) && topDownSearchValid(node.left, low, node.val) && topDownSearchValid(node.right, node.val, high);
      }
    }

    /**
     * For a binary search tree, if you do a in-order search, it'll give you
     * the inscreasing-order sequence.
     */
    public boolean isValidBSTByInOrderIterativeSearch(TreeNode root) {
      if (root == null) {
        return true;
      }

      Stack<TreeNode> stack = new Stack<>();
      TreeNode current = root;

      while(current != null) {
        stack.push(current);
        current = current.left;
      }

      Integer previousValue = null;
      while(!stack.empty()) {
        current = stack.pop();
        if (previousValue != null && current.val <= previousValue) {
          return false;
        }
        previousValue = current.val;

        /* if there is a right subtree, move to the left-most node on the subtree */
        if (current.right != null) {
          TreeNode node = current.right;
          while(node != null) {
            stack.push(node);
            node = node.left;
          }
        }
      }

      return true;
    }

    /**
     *  when use recursive in-order, we need to have a record of previous node
     */
    private TreeNode previous;
    public boolean isValidBSTByInOrderRecursiveSearch(TreeNode root) {
      previous = null;
      return isValid(root)
    }

    private isValid(node) {
      if (node == null) {
        return true;
      }

      if (isValid(node.left)) {
        if (previous != null && node.val <= previous.val) {
          return false;
        }
        previous = node;
        return isValid(node.right);
      } else {
        return false;
      }
    }
}

package javasolutions.p110;

import javasolutions.TreeNode;
import java.util.Queue;
import java.util.LinkedList;

public class BalancedBinaryTree {
  public boolean isBalanced(TreeNode root) {
    if (root == null) {
      return true;
    }

    Queue<TreeNode> queue = new LinkedList<>();
    queue.offer(root);

    while(!queue.isEmpty()) {
      TreeNode node = queue.poll();

      if (Math.abs(depth(node.left) - depth(node.right)) > 1) {
        return false;
      }
      
      if (node.left != null) {
        queue.offer(node.left);
      }

      if (node.right != null) {
        queue.offer(node.right);
      }
    }

    return true;
  }

  private int depth(TreeNode root) {
    if (root == null) {
      return 0;
    }

    return Math.max(depth(root.left), depth(root.right)) + 1; 
  }

  /**
   * Use -1 as depth to indicate that the tree rooted at this input node is not
   * a balanced binary tree. And if subtree is not a binary tree, then the tree
   * rooted at the current node is not a balanced binary tree.
   */
  
  public boolean isBalancedFaster(TreeNode root) {
    return depthFaster(root) != -1;
  }

  private int depthFaster(TreeNode root) {
    if (root == null) {
      return 0;
    }

    int leftDepth = depthFaster(root.left);
    if (leftDepth == -1 ) {
      return -1;
    }

    int rightDepth = depthFaster(root.right);
    if (rightDepth == -1) {
      return -1;
    }

    if (Math.abs(leftDepth - rightDepth) > 1) {
      return -1;
    } else {
      return Math.max(leftDepth, rightDepth) + 1;
    }
  }

  public static void main(String[] args) {
    TreeNode root = TreeNode.dummyTree();
    BalancedBinaryTree bbt = new BalancedBinaryTree();
    System.out.println(bbt.isBalanced(root));
    System.out.println(bbt.isBalancedFaster(root));
  }
}
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

  public static void main(String[] args) {
    TreeNode root = TreeNode.dummyTree();
    BalancedBinaryTree bbt = new BalancedBinaryTree();
    System.out.println(bbt.isBalanced(root));
  }
}
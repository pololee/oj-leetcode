package javasolutions.p111;

import javasolutions.TreeNode;
import java.util.LinkedList;
import java.util.Queue;

public class MinimumDepthOfBinaryTree {
  public int minDepth(TreeNode root) {
    if (root == null) {
      return 0;
    }

    if (root.left == null && root.right != null) {
    return minDepth(root.right) + 1;
    }

    if (root.right == null && root.left != null) {
    return minDepth(root.left) + 1;
    }

    return Math.min(minDepth(root.left), minDepth(root.right)) + 1;
  }

  public int minDepthByBFS(TreeNode root) {
    if (root == null) {
      return 0;
    }

    Queue<TreeNode> queue = new LinkedList<>();
    queue.offer(root);
    TreeNode rightMost = root;
    int depth = 1;

    while (!queue.isEmpty()) {
      TreeNode node = queue.poll();

      if (node.left == null && node.right == null) {
        break;
      }

      if (node.left != null) {
        queue.offer(node.left);
      }

      if (node.right != null) {
        queue.offer(node.right);
      }

      // node == rightMost, and the loop doesn't break at line 38, which means
      // the next level exists, so we do depth++;
      if (rightMost == node) {
        depth++;
        rightMost = node.right != null ? node.right : node.left;
      }
    }

    return depth;
  }

  public static void main(String[] args) {
    TreeNode root = TreeNode.dummyTree();
    MinimumDepthOfBinaryTree cal = new MinimumDepthOfBinaryTree();
    int depth = cal.minDepth(root);
    System.out.println(depth);
    System.out.println(cal.minDepthByBFS(root));
  }
}

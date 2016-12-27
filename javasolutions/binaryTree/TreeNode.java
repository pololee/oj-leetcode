package javasolutions.binaryTree;

import java.util.LinkedList;
import java.util.Queue;

public class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;

  public TreeNode(int x, TreeNode leftNode, TreeNode rightNode) {
    val = x;
    left = leftNode;
    right = rightNode;
  }

  public TreeNode(int x) {
    this(x, null, null);
  }

  /**
   * 							1
   * 				2	 					3
   * 		4			  5  						6
   *   			 7
   */

  public static TreeNode dummyTree() {
    TreeNode root = new TreeNode(1);
    root.left = new TreeNode(2);
    root.right = new TreeNode(3);
    root.left.left = new TreeNode(4);
    root.left.right = new TreeNode(5);
    root.right.right = new TreeNode(6);
    root.left.right.left = new TreeNode(7);

    return root;
  }

  public static void main(String[] args) {
    TreeNode root = TreeNode.dummyTree();

    Queue<TreeNode> queue = new LinkedList<>();
    queue.offer(root);

    StringBuilder builder = new StringBuilder();

    while(!queue.isEmpty()) {
      TreeNode node = queue.poll();
      builder.append(String.valueOf(node.val)).append(" ");

      if(node.left != null) queue.offer(node.left);
      if(node.right != null) queue.offer(node.right);
    }

    builder.deleteCharAt(builder.length() - 1);
    System.out.println(builder.toString());
  }
}
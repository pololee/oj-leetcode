/**
 * Reference: http://bangbingsyb.blogspot.com/2014/11/leetcode-binary-tree-maximum-path-sum.html
 *
 * Important notes:
 *
 * 1. Bottom up approach
 * 2. Categorize all the paths into two classes:
 *   Given the current node,
 *     a: path end to the current node(from either left subtree or right subtree)
 *     b: path cross the current node
 */

package javasolutions.p124;

import javasolutions.TreeNode;

public class BTMaximumPathSum {
  private int maxSum;

  public int maxPathSum(TreeNode root) {
    maxSum = Integer.MIN_VALUE;
    findMaxSum(root);

    return maxSum;
  }

  private int findMaxSum(TreeNode node) {
    if (node == null) {
      return 0;
    }

    /**
     * Compare the result to 0, because if it's < 0, then there is no point to give
     * back the negative value to construct the maxSum. Just return 0
     */
    int leftPathEndToNodeMaxSum = 0, rightPathEndToNodeMaxSum = 0;
    if (node.left != null) {
      leftPathEndToNodeMaxSum = Math.max(findMaxSum(node.left), 0);
    }

    if (node.right != null) {
      rightPathEndToNodeMaxSum = Math.max(findMaxSum(node.right), 0);
    }

    int endToNodeMaxSum = Math.max(leftPathEndToNodeMaxSum, rightPathEndToNodeMaxSum) + node.val;
    int crossNodeMaxSum = leftPathEndToNodeMaxSum + node.val + rightPathEndToNodeMaxSum;
    maxSum = Math.max(maxSum, Math.max(endToNodeMaxSum, crossNodeMaxSum));

    /**
     * return the a-class path, because b-class path cannot be used to construct
     * the new path with the parent node.
     */
    return endToNodeMaxSum;
  }

  public static void main(String[] args) {
    TreeNode root = new TreeNode(1);
    root.left = new TreeNode(2);
    root.right = new TreeNode(3);

    BTMaximumPathSum finder = new BTMaximumPathSum();
    System.out.println(finder.maxPathSum(root));
  }
}
package javasolutions.p124;

import javasolutions.TreeNode;

public class BTMaxPathSumBetter {
  public int maxPathSum(TreeNode root) {
    maxSum = Integer.MIN_VALUE;
    findMax(root);

    return maxSum;
  }

  private int maxSum;

  // Given a node, the potential maximum path sum cases:
  // 1. max(left subtree) + node.val   (the path ends at the current node)
  // 2. max(right subtree) + node.val  (the path ends at the current node)
  // 3. max(left subtree) + node.val + max(right subtree)  (the path cross the current node)
  // 4. the node.val itself (the path only includes the current node)
  //
  // More thoughts, when calculate case 1 and 2
  // max(left subtree) should return the maxSum of path that ends at current.leftChild
  // max(right subtree) should return the maxSum of path that ends at current.rightChild
  //
  // if max(left subtree) < 0, then just let max(left subtree) return 0 because it doesn't 
  // contribute anything to make the current node's sum larger
  private int findMaxEndsAtMe(TreeNode root) {
    if(root == null) return 0;

    int maxSumEndsAtMyLeftChild = findMax(root.left);
    int maxSumEndsAtMyRightChild = findMax(root.right);

    // Since maxSumEndsAtMyLeftChild and maxSumEndsAtMyRightChild are at least 0,
    //  maxSumEndsAtMyLeftChild + root.val + maxSumEndsAtMyRightChild is definitely going to be larger that maxSumEndsAtMe
    maxSum = Math.max(maxSum, maxSumEndsAtMyLeftChild + root.val + maxSumEndsAtMyRightChild);
    
    int maxSumEndsAtMe = Math.max(maxSumEndsAtMyLeftChild, maxSumEndsAtMyRightChild) + root.val;
    return maxSumEndsAtMe > 0 ? maxSumEndsAtMe : 0;
  }
}
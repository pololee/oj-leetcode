/**
https://leetcode.com/problems/kth-smallest-element-in-a-bst/#/description
 */

package javasolutions.p230;

import javasolutions.TreeNode;
import java.util.Stack;

public class KthSmallestElementInBST {
  public int kthSmallest(TreeNode root, int k) {
    if(root == null) return 0;

    Stack<TreeNode> stack = new Stack<>();
    TreeNode node = root;
    while(node != null) {
      stack.push(node);
      node = node.left;
    }

    int index = 0;
    while(!stack.isEmpty()) {
      node = stack.pop();
      index++;

      if(index == k) {
        return node.val;
      }

      if(node.right != null) {
        node = node.right;

        while(node != null) {
          stack.push(node);
          node = node.left;
        }
      }
    }

    return 0;
  }

  public int kthSmallestBetter(TreeNode root, int k) {
    if(root == null) return 0;

    Stack<TreeNode> stack = new Stack<>();
    TreeNode node = root;
    int count = 0;

    while(node != null || !stack.isEmpty()) {
      while(node != null) {
        stack.push(node);
        node = node.left;
      }

      node = stack.pop();
      count++;

      if(count == k) {
        return node.val;
      }

      node = node.right;
    }

    return 0;
  }

  public static void main(String[] args) {
    TreeNode root = new TreeNode(5);
    root.left = new TreeNode(4);
    root.right = new TreeNode(6);

    KthSmallestElementInBST cal = new KthSmallestElementInBST();
    System.out.println(cal.kthSmallest(root, 1));
    System.out.println(cal.kthSmallest(root, 2));
    System.out.println(cal.kthSmallest(root, 3));
  }
}
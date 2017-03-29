/**
https://leetcode.com/problems/binary-search-tree-iterator/#/description
*/

package javasolutions.p173;

import javasolutions.TreeNode;
import java.util.Stack;

public class BSTIterator {
  private Stack<TreeNode> stack;

  public BSTIterator(TreeNode root) {
    stack = new Stack<>();
    TreeNode pointer = root;

    while(pointer != null) {
      stack.push(pointer);
      pointer = pointer.left;
    }
  }

  public boolean hasNext() {
    return !stack.isEmpty();
  }

  public int next() {
    TreeNode node = stack.pop();
    int answer = node.val;

    if(node.right != null) {
      node = node.right;
      while(node != null) {
        stack.push(node);
        node = node.left;
      }
    }

    return answer;
  }
}
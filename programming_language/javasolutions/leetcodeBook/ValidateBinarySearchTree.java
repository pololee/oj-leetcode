// Somehow, they consider an empty tree as a valid BST

package javasolutions.leetcodeBook;

import javasolutions.TreeNode;
import java.util.Stack;

public class ValidateBinarySearchTree {
  public boolean isValidBST(TreeNode root) {
    return false;
  }

  public boolean isValidByInOrderTravel(TreeNode root) {
    if(root == null) return true;

    Stack<TreeNode> stack = new Stack<>();
    TreeNode node = root;
    while(node != null) {
      stack.push(node);
      node = node.left;
    }

    TreeNode previous = null;
    while(!stack.empty()) {
      TreeNode current = stack.pop();

      if(previous != null && current.val <= previous.val) return false;
      
      if(current.right != null) {
        TreeNode tmp = current.right;
        while(tmp != null) {
          stack.push(tmp);
          tmp = tmp.left;
        }
      }

      previous = current;
    }

    return true;
  }

  public boolean isValidInOrderRecursive(TreeNode root) {
    if(root == null) return true;
    return isValid(root);
  }

  private TreeNode previous;
  private boolean isValid(TreeNode root) {
    if(root == null) return true;

    if(isValid(root.left)) {
      if(previous != null && previous.val >= root.val) {
        return false;
      }
      previous = root;
      return isValid(root.right);
    } else {
      return false;
    }
  }

  public static void main(String[] args) {
    TreeNode root = new TreeNode(2);
    root.left = new TreeNode(1);
    root.right = new TreeNode(3);

    ValidateBinarySearchTree cal = new ValidateBinarySearchTree();
    System.out.println(cal.isValidByInOrderTravel(root));
    System.out.println(cal.isValidInOrderRecursive(root));

    TreeNode root2 = new TreeNode(1);
    root2.left = new TreeNode(2);
    root2.right = new TreeNode(3);

    System.out.println(cal.isValidByInOrderTravel(root2));
    System.out.println(cal.isValidInOrderRecursive(root));
  }
}
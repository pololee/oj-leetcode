package javasolutions.p257;

/**
 https://leetcode.com/problems/binary-tree-paths/#/description
 */

import javasolutions.TreeNode;
import java.util.List;
import java.util.ArrayList;

public class BinaryTreePaths {
  public List<String> binaryTreePaths(TreeNode root) {
    if(root == null) return null;

    List<String> answer = new ArrayList<>();
    dfs(root, "", answer);

    return answer;
  }

  private void dfs(TreeNode root, String output, List<String> answer) {
    output += String.valueOf(root.val);

    if(root.left == null && root.right == null) {
      answer.add(output);
    } else {
      if(root.left != null) dfs(root.left, output + "->", answer);
      if(root.right != null) dfs(root.right, output + "->", answer);
    }
  }

  public static void main(String[] args) {
    TreeNode root = new TreeNode(1);
    root.left = new TreeNode(2);
    root.right = new TreeNode(3);
    root.left.right = new TreeNode(5);

    BinaryTreePaths cal = new BinaryTreePaths();
    List<String> result = cal.binaryTreePaths(root);
    System.out.println(result.toString());
  }
}
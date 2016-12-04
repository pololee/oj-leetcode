package javasolutions.p108;

import javasolutions.TreeNode;

public class SortedArrayToBST {
  public TreeNode convert(int[] nums) {
    if (nums.length == 0) {
      return null;
    }
    
    return convertToBST(nums, 0, nums.length - 1);
  }

  private TreeNode convertToBST(int[] numbers, int low, int high) {
    int middle = (low + high) / 2;

    TreeNode root = new TreeNode(numbers[middle]);
    
    if (middle > low) {
      root.left = convertToBST(numbers, low, middle - 1);
    }

    if (middle < high) {
      root.right = convertToBST(numbers, middle + 1, high);
    }

    return root;
  }
}
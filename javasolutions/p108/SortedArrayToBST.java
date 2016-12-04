package javasolutions.p108;

import javasolutions.TreeNode;

public class SortedArrayToBST {
  public TreeNode convert(int[] nums) {
    return convertToBST(nums, 0, nums.length - 1);
  }

  private TreeNode convertToBST(int[] numbers, int low, int high) {
    if (low > high) {
      return null;
    }

    int middle = (low + high) / 2;

    TreeNode root = new TreeNode(numbers[middle]);
    root.left = convertToBST(numbers, low, middle - 1);
    root.right = convertToBST(numbers, middle + 1, high);

    return root;
  }
}
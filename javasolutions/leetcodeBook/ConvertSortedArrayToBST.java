package javasolutions.leetcodeBook;

import javasolutions.TreeNode;

public class ConvertSortedArrayToBST {
  public TreeNode sortedArrayToBST(int[] nums) {

  }

  private TreeNode sortedArrayToBSTHelper(int[] nums, int low, int high) {
    if(low > high) return null;

    int middle = (low + high) / 2;
    TreeNode root = new TreeNode(nums[middle]);
    root.left = sortedArrayToBSTHelper(nums, low, middle-1);
    root.right = sortedArrayToBSTHelper(nums, middle + 1, high);
    return root;
  }
}
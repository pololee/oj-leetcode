/**
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/#/description

Given an array where elements are sorted in ascending order,
convert it to a height balanced BST.
 */

package airbnb.p108;

public class Solution {
  public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    public TreeNode(int x) {
      val = x;
    }
  }
  public TreeNode sortedArrayToBST(int[] nums) {
    if(nums == null || nums.length == 0) return null;

    return convertToBST(nums, 0, nums.length - 1);
  }

  private TreeNode convertToBST(int[] nums, int start, int end) {
    if(start > end) return null;

    int middle = start + (end - start) / 2;
    TreeNode root = new TreeNode(nums[middle]);
    root.left = convertToBST(nums, start, middle - 1);
    root.right = convertToBST(nums, middle + 1, end);

    return root;
  }
}
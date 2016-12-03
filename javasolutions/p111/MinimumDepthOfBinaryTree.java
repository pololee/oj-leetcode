package javasolutions.p111;

import javasolutions.TreeNode;

public class MinimumDepthOfBinaryTree {
	public int minDepth(TreeNode root) {
		if (root == null) {
			return 0;
		}

		if (root.left == null && root.right != null) {
			return minDepth(root.right) + 1;
		}

		if (root.right == null && root.left != null) {
			return minDepth(root.left) + 1;
		}

		return Math.min(minDepth(root.left), minDepth(root.right)) + 1;
	}

	public static void main(String[] args) {
		TreeNode root = TreeNode.dummyTree();
		MinimumDepthOfBinaryTree cal = new MinimumDepthOfBinaryTree();
		int depth = cal.minDepth(root);
		System.out.println(depth);
	}
}
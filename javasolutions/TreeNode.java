package javasolutions;

public class TreeNode {
  public int val;
  public TreeNode left;
  public TreeNode right;

  public TreeNode(int x) {
    val = x;
  }

  public static TreeNode dummyTree() {
  	TreeNode root = new TreeNode(1);

  	root.left = new TreeNode(2);
  	root.right = new TreeNode(6);

  	root.left.left = new TreeNode(3);
  	root.left.right = new TreeNode(4);
  	root.right.right = new TreeNode(7);

  	root.left.right.left = new TreeNode(5);
  	return root;
  }
}
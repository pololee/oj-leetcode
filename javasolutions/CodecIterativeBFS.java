package javasolutions;

import java.util.LinkedList;
import java.util.Queue;

public class CodecIterativeBFS {
	public String serialize(TreeNode root) {
		if (root == null) {
			return null;
		}

		Queue<TreeNode> nodeQueue = new LinkedList<TreeNode>();
		StringBuilder builder = new StringBuilder();

		nodeQueue.add(root);
		while(!nodeQueue.isEmpty()) {
			TreeNode node = nodeQueue.poll();
			builder.append(node.val).append(",");

			if(node.left == null) {
				builder.append("#,");
			} else {
				nodeQueue.add(node.left);
			}

			if (node.right == null) {
				builder.append("#,");
			} else {
				nodeQueue.add(node.right);
			}
		}

		builder.deleteCharAt(builder.length() - 1);
		return builder.toString();
	}

	public TreeNode deserialize(String data) {

	}

	public static void main(String[] args) {
		CodecIterativeBFS codec = new CodecIterativeBFS();

    TreeNode root = new TreeNode(1);
    root.left = new TreeNode(2);
    root.right = new TreeNode(3);
    root.right.left = new TreeNode(4);
    root.right.right = new TreeNode(5);

    String str = codec.serialize(root);
    System.out.println(str);
	}
}
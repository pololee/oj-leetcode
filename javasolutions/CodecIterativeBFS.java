package javasolutions;

import java.util.LinkedList;

public class CodecIterativeBFS {
	public String serialize(TreeNode root) {
		if (root == null) {
			return null;
		}

		LinkedList<TreeNode> nodeQueue = new LinkedList<TreeNode>();
		StringBuilder builder = new StringBuilder();

		nodeQueue.add(root);
		while(!nodeQueue.isEmpty()) {
			TreeNode node = nodeQueue.poll();

			if (node == null) {
				builder.append("#,");
			} else {
				builder.append(node.val).append(",");
				nodeQueue.add(node.left);
				nodeQueue.add(node.right);
			}
		}

		builder.deleteCharAt(builder.length() - 1);
		return builder.toString();
	}

	public TreeNode deserialize(String data) {
		if (data == null || data.isEmpty()) {
			return null;
		}

		String[] strArray = data.split(",");
		TreeNode root = new TreeNode(Integer.parseInt(strArray[0]));
		LinkedList<TreeNode> nodeQueue = new LinkedList<TreeNode>();
		nodeQueue.add(root);

		int i = 1;
		while(!nodeQueue.isEmpty() && i < strArray.length) {
			TreeNode current = nodeQueue.poll();

			if (current == null) {
				continue;
			}

			if (strArray[i].equals("#")) {
				current.left = null;
				nodeQueue.add(null);
			} else {
				current.left = new TreeNode(Integer.parseInt(strArray[i]));
				nodeQueue.add(current.left);
			}

			i++;
			if (i >= strArray.length) {
				break;
			}

			if (strArray[i].equals("#")) {
				current.right = null;
				nodeQueue.add(null);
			} else {
				current.right = new TreeNode(Integer.parseInt(strArray[i]));
				nodeQueue.add(current.right);
			}
			i++;
		}
		return root;
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
    System.out.println("deserialize and serialize again:");
    System.out.println(codec.serialize(codec.deserialize(str)));
	}
}
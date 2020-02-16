package javasolutions.learn;

import java.util.Stack;

public class BTInOrderTraversal<T> {
	public void recursiveTraversal(BTNode<T> root) {
		if (root == null) {
			return;
		}

		String results = new String();
		results = recurisveHelper(root, results);

		System.out.println(results);
	}

	private String recurisveHelper(BTNode<T> root, String output) {
		if (root == null) {
			return "";
		} else {
			output = recurisveHelper(root.left, output);
			output = output + root.toString() + " ";
			output = output + recurisveHelper(root.right, output);
		}

		return output;
	}

	public void iterativeTraversal(BTNode<T> root) {
		if (root == null) {
			return;
		}

		StringBuilder builder = new StringBuilder();
		Stack<BTNode<T>> stack = new Stack<>();
		BTNode<T> current = root;

		// find the first node should be visited (left-most in the tree)
		while(current != null) {
			stack.push(current);
			current = current.left;
		}

		while(!stack.empty()) {
			current = stack.pop();
			builder.append(current.toString()).append(" ");

			if (current.right != null) {
				current = current.right;

				// find the left-most node on the right-subtree on the current node
				while(current != null) {
					stack.push(current);
					current = current.left;
				}
			}
		}

		// while(!stack.empty() || current != null) {
		// 	while(current != null) {
		// 		stack.push(current);
		// 		current = current.left;
		// 	}

		// 	current = stack.pop();
		// 	builder.append(current.toString()).append(" ");
		// 	current = current.right;
		// }

		builder = builder.deleteCharAt(builder.length() - 1);
		System.out.println(builder.toString());
	}

	public static void main(String[] args) {
		BTNode<String> root = BTNode.<String>dummyTree();
		BTInOrderTraversal<String> travel = new BTInOrderTraversal<>();
		travel.recursiveTraversal(root);
		travel.iterativeTraversal(root);
	}
}
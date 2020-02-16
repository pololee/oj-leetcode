/**
 * http://www.geeksforgeeks.org/iterative-postorder-traversal/
 *
 *   take a look at the following tree
 *   							1
 *          2						3
 *     4			5				6			7
 *
 * PostOrderTraversal: 4 5 2 6 7 3 1
 * The sequence we need to push the stack: 1 3 7 6 2 5 4
 * PreOrderTraversal: 1 2 4 5 3 6 7
 * InPreOrderTraversal, if we visit right node first, then left node: 1 3 7 6 2 5 4
 * which is exactly what we need
 *
 * So we can have two stacks:
 * First to have preOrder(right first, then left):
 *
 * 1. Push root to first stack.
 * 2. Loop while first stack is not empty
 * 	2.1 Pop a node from first stack and push it to second stack
 *  2.2 Push left and right children of the popped node to first stack
 * 3. Print contents of second stack
 *
 */

/**
 * http://algorithmsandme.in/2015/03/post-order-traversal-of-binary-search-tree-without-recursion/
 *
 * Looking at recursiveHelper, it is clear that parent node is visited twice,
 * once coming up from left sub tree and second time when coming up from right sub tree.
 * However, parent node is to be printed when we have already printed left as well as right child.
 * So, we need to keep track of the previous visited node.
 *
 * There are tree values possible for previous node:
 *  1.Previous node is parent of current node,that means we are traversing tree downwards.
 *    No need to do anything with the current node.
 *  2.Previous node is left child of current node, that means we have already visited left child,
 *    but still not have visited right child,hence we move to right child of current node.
 *  3.Previous node is right child of current node, left and right child of current node are already visited.
 *    hence all we need to do is to print current node.
 */

package javasolutions.learn;

import java.util.Stack;

public class BTPostOrderTraversal<T> {
	/**
	 * [recursiveTraversal description]
	 * @param root [description]
	 */
	public void recursiveTraversal(BTNode<T> root) {
		if (root == null) {
			return;
		}

		String results = new String();
		results = recursiveHelper(root, results);
		System.out.println(results);
	}

	private String recursiveHelper(BTNode<T> node, String output) {
		if (node == null) {
			return "";
		} else {
			output = recursiveHelper(node.left, output);
			output = output + recursiveHelper(node.right, output);
			output = output + node.toString() + " ";
		}

		return output;
	}

	/**
	 * [iterativeTraversalWithTwoStacks description]
	 * @param root [description]
	 */
	public void iterativeTraversalWithTwoStacks(BTNode<T> root) {
		if (root == null) {
			return;
		}

		StringBuilder builder = new StringBuilder();
		Stack<BTNode<T>> rightFirstPreOrderStack = new Stack<>();
		Stack<BTNode<T>> stack = new Stack<>();
		rightFirstPreOrderStack.push(root);

		while(!rightFirstPreOrderStack.empty()) {
			BTNode<T> current = rightFirstPreOrderStack.pop();
			stack.push(current);

			if (current.left != null) {
				rightFirstPreOrderStack.push(current.left);
			}

			if (current.right != null) {
				rightFirstPreOrderStack.push(current.right);
			}
		}

		while(!stack.empty()) {
			BTNode<T> node = stack.pop();
			builder.append(node.toString()).append(" ");
		}

		builder.deleteCharAt(builder.length() - 1);
		System.out.println(builder.toString());
	}

	/**
	 * [iterativeTraversalWithOneStack description]
	 * @param root [description]
	 */
	public void iterativeTraversalWithOneStack(BTNode<T> root) {
		if (root == null) {
			return;
		}

		StringBuilder builder = new StringBuilder();
		Stack<BTNode<T>> stack = new Stack<>();
		stack.push(root);
		BTNode<T> previous = null;

		while(!stack.empty()) {
			// look up without removing the element
			BTNode<T> current = stack.peek();

			/* case 1: Moving down the tree */
			if (previous == null || previous.left == current || previous.right == current) {
				if (current.left != null) {
					stack.push(current.left);
				} else if (current.right != null) {
					stack.push(current.right);
				} else {
					builder.append(current.toString()).append(" ");
					stack.pop();
				}
			}

			/* case 2: Moving up from the left substree */
			if (previous == current.left) {
				if (current.right != null) {
					stack.push(current.right);
				} else {
					builder.append(current.toString()).append(" ");
					stack.pop();
				}
			}

			/* case 3: Moving up from the right substree */
			if (previous == current.right) {
				builder.append(current.toString()).append(" ");
				stack.pop();
			}

			previous = current;
		}

		builder.deleteCharAt(builder.length() - 1);
		System.out.println(builder.toString());
	}

	public static void main(String[] args) {
		BTNode<String> root = BTNode.<String>dummyTree();
		BTPostOrderTraversal<String> travel = new BTPostOrderTraversal<>();
		travel.recursiveTraversal(root);
		travel.iterativeTraversalWithTwoStacks(root);
		travel.iterativeTraversalWithOneStack(root);
	}
}
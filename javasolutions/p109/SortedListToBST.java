package javasolutions.p109;

import javasolutions.TreeNode;
import javasolutions.ListNode;

public class SortedListToBST {

	/**
	 * We build the tree from bottom up.
	 *
	 * We need this listPointer, because we reply on convertToBST to move the
	 * listPointer.
	 */
	private ListNode listPointer;

  public TreeNode convert(ListNode head) {
  	if (head == null) {
  		return null;
  	}

  	int size = 0;
  	ListNode current = head;
  	while(current != null) {
  		size++;
  		current = current.next;
  	}

  	listPointer = head;
  	return convertToBST(0, size - 1);
  }

  private TreeNode convertToBST(int start, int end) {
  	if (start > end) {
  		return null;
  	}

  	int middle = (start + end)/2;
  	TreeNode leftChild = convertToBST(start, middle - 1);

  	TreeNode parent = new TreeNode(listPointer.val);
  	parent.left = leftChild;

  	listPointer = listPointer.next;
  	TreeNode rightChild = convertToBST(middle + 1, end);
  	parent.right = rightChild;

  	return parent;
  }

  private void printTree(TreeNode root) {
  	if (root == null) {
  		return;
  	}

  	printTree(root.left);
  	System.out.println(String.valueOf(root.val) + " ");
  	printTree(root.right);
  }

  public static void main(String[] args) {
  	ListNode head = new ListNode(1);
  	head.next = new ListNode(2);
  	head.next.next = new ListNode(3);
  	head.next.next.next = new ListNode(4);

  	SortedListToBST converter = new SortedListToBST();
  	TreeNode root = converter.convert(head);
  	converter.printTree(root);
  }
}
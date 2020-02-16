package javasolutions.leetcodeBook;

import javasolutions.ListNode;
import javasolutions.TreeNode;

public class ConvertSortedListToBST {
  public TreeNode sortedListToBST(ListNode head) {
    if(head == null) return null;

    int start = 0;
    int end = 0;
    ListNode pointer = head;
    while(pointer != null) {
      end++;
      pointer = pointer.next;
    }

    listPointer = head;
    return convert(start, end - 1);
  }

  private ListNode listPointer;
  
  private TreeNode convert(int start, int end) {
    if(start > end) return null;

    int middle = (start + end)/2;
    TreeNode leftChild = convert(start, middle - 1);

    TreeNode root = new TreeNode(listPointer.val);
    root.left = leftChild;

    root.right = convert(middle + 1, end);
    return root;
  }
}
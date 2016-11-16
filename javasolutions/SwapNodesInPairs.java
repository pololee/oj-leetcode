/**
 * What if the number of nodes in the linked list has only odd number of nodes?
 * The last node should not be swapped.
 */

package javasolutions;

public class SwapNodesInPairs {
  public ListNode swapPairs(ListNode head) {
    ListNode dummyHead = new ListNode(0);
    dummyHead.next = head;

    ListNode prev = dummyHead;
    ListNode current = head;

    while (current != null && current.next != null) {
      ListNode x = current;
      ListNode y = current.next;
      prev.next = y;
      x.next = y.next;
      y.next = x;
      prev = x;
      current = x.next;
    }

    return dummyHead.next;
  }
}

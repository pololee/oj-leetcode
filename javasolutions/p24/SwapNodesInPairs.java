package javasolutions.p24;

import javasolutions.ListNode;

// Swap needs three pointer, previous, current, next

public class SwapNodesInPairs {
  public ListNode swapPairs(ListNode head) {
    if(head == null) return null;

    ListNode dummyHead = new ListNode(0);
    dummyHead.next = head;

    ListNode previous = dummyHead;
    ListNode current = head;

    while(current != null && current.next != null) {
      ListNode next = current.next;

      current.next = next.next;
      next.next = current;
      previous.next = next;

      previous = current;
      current = current.next;
    }

    return dummyHead.next;
  }

  private void print(ListNode head) {
    if(head == null) {
      System.out.println("[]");
    } else {
      while(head != null) {
        System.out.print(String.format("%d ", head.val));
        head = head.next;
      }
    }

    System.out.println();
  }

  public static void main(String[] args) {
    ListNode head = new ListNode(1);
    head.next = new ListNode(2);
    head.next.next = new ListNode(3);

    SwapNodesInPairs cal = new SwapNodesInPairs();
    ListNode result = cal.swapPairs(head);
    cal.print(result);
  }
}
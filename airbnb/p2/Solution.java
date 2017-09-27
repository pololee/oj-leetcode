/**
 * https://leetcode.com/problems/add-two-numbers/#/description
 */

package airbnb.p2;

public class Solution {
  public class ListNode {
    int val;
    ListNode next;

    public ListNode(int x) {
      val = x;
    }
  }

  public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    ListNode dummyHead = new ListNode(0);
    ListNode current = dummyHead;
    int sum = 0;
    int carry = 0;

    while(l1 != null || l2 != null) {
      int a = (l1 != null) ? l1.val : 0;
      int b = (l2 != null) ? l2.val : 0;

      sum = a + b + carry;
      current.next = new ListNode(sum % 10);
      carry = sum / 10;

      if(l1 != null) l1 = l1.next;
      if(l2 != null) l2 = l2.next;
      current = current.next;
    }

    if(carry != 0) {
      current.next = new ListNode(1);
    }

    return dummyHead.next;
  }
}

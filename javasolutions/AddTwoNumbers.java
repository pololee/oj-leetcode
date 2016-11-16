package javasolutions;

public class AddTwoNumbers {
  public ListNode addTwoNumbers (ListNode num1, ListNode num2) {
    ListNode dummyHead = new ListNode(0);
    ListNode current = dummyHead;

    int carry = 0;
    while (num1 != null || num2 != null) {
      int val1 = (num1 == null) ? 0 : num1.val;
      int val2 = (num2 == null) ? 0 : num2.val;
      int sum = val1 + val2 + carry;

      if (sum < 10) {
        current.next = new ListNode(sum);
        carry = 0;
      } else {
        current.next = new ListNode(sum % 10);
        carry = 1;
      }

      if (num1 != null) {
        num1 = num1.next;
      }

      if (num2 != null) {
        num2 = num2.next;
      }

      current = current.next;
    }

    if (carry != 0) {
      current.next = new ListNode(1);
    }

    return dummyHead.next;
  }
}

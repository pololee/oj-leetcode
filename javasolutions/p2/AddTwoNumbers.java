package javasolutions.p2;

import javasolutions.ListNode;

public class AddTwoNumbers {
  public ListNode addTwoNumbers(ListNode num1, ListNode num2) {
    ListNode dummyHead = new ListNode(0);
    ListNode pointer = dummyHead;
    
    int sum = 0, remainder = 0;
    while(num1 != null && num2 != null) {
      sum = num1.val + num2.val + remainder;
      
      num1.val = sum % 10;
      pointer.next = num1;
      pointer = pointer.next;

      remainder = sum / 10;

      num1 = num1.next;
      num2 = num2.next;
    }

    while(num1 != null) {
      sum = num1.val + remainder;

      num1.val = sum % 10;
      pointer.next = num1;
      pointer = pointer.next;

      remainder = sum / 10;
      num1 = num1.next;
    }

    while(num2 != null) {
      sum = num2.val + remainder;

      num2.val = sum % 10;
      pointer.next = num2;
      pointer = pointer.next;

      remainder = sum / 10;
      num2 = num2.next;
    }

    if(remainder > 0) {
      pointer.next = new ListNode(remainder);
    }

    return dummyHead.next;
  }

  public ListNode addTwoNumbersBetter(ListNode num1, ListNode num2) {
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
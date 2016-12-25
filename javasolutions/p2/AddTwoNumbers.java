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
}
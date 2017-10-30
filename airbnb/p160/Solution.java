/**
https://leetcode.com/problems/intersection-of-two-linked-lists/#/description

Write a program to find the node at which the intersection of two singly linked lists begins.

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
 */

package airbnb.p160;

public class Solution {
  public class ListNode {
    int val;
    ListNode next;

    public ListNode(int x) {
      val = x;
      next = null;
    }
  }

  public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
    if(headA == null || headB == null) return null;

    int lengthA = getLength(headA);
    int lengthB = getLength(headB);
    ListNode pointerA = headA;
    ListNode pointerB = headB;

    if(lengthA > lengthB) {
      int diff = lengthA - lengthB;
      while(diff != 0) {
        pointerA = pointerA.next;
        diff--;
      }
    } else if(lengthB > lengthA) {
      int diff = lengthB - lengthA;
      while(diff != 0) {
        pointerB = pointerB.next;
        diff--;
      }
    }

    while(pointerA != null && pointerB != null && pointerA != pointerB) {
      pointerA = pointerA.next;
      pointerB = pointerB.next;
    }

    if(pointerA != null && pointerB != null) {
      return pointerA;
    } else {
      return null;
    }
  }

  private int getLength(ListNode head) {
    if(head == null) return 0;

    int length = 0;
    ListNode pointer = head;
    while(pointer != null) {
      length++;
      pointer = pointer.next;
    }

    return length;
  }

  // Soluton 2 is genius http://www.cnblogs.com/grandyang/p/4128461.html
  // we have two pointers A, B for each list and start running
  // if one of the pointers reach the end, then move the pointer to point
  // the start of the other list. Keep running and those two pointers will be equal
  // two cases:
  // 1. no intersection, then the pointers just point to the end of each list
  // 2. has intersection, then the pointers point to the intersection
  // Why?
  // because two pointers are running at the same speed, one step each time.
  // and they have run the same length (the sum of two lists' length)
  public ListNode getIntersectionNodePro(ListNode headA, ListNode headB) {
    if(headA == null || headB == null) return null;

    ListNode pointerA = headA;
    ListNode pointerB = headB;

    while(pointerA != pointerB) {
      pointerA = (pointerA != null) ? pointerA.next : headB;
      pointerB = (pointerB != null) ? pointerB.next : headA;
    }

    return pointerA;
  }
}

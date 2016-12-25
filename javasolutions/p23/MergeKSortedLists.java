package javasolutions.p23;

import javasolutions.ListNode;

public class MergeKSortedLists {
  public ListNode mergeKLists(ListNode[] lists) {
    int begin = 0, end = lists.length - 1;

    while(end > 0) {
      begin = 0;

      while(end > begin) {
        lists[begin] = mergeTwoLists(lists[begin], lists[end]);
        begin++;
        end--;
      }
    }

    return lists[0];
  }

  private ListNode mergeTwoLists(ListNode l1, ListNode l2) {
    ListNode dummyHead = new ListNode(0);
    ListNode pointer = dummyHead;

    while(l1 != null && l2 != null) {
      if(l1.val <= l2.val) {
        pointer.next = l1;
        l1 = l1.next;
      } else {
        pointer.next = l2;
        l2 = l2.next;
      }

      pointer = pointer.next;
    }

    if(l1 != null) pointer.next = l1;
    if(l2 != null) pointer.next = l2;

    return dummyHead.next;
  }
}
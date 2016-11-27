package javasolutions;

import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Comparator;

public class MergeKSortedLinkedLists {

  /*
  Use minimum Heap, insert a new node to minHeap takes O(logn)
  */
  public ListNode mergeKListsWithHeap(ListNode[] lists) {
    ListNode dummyHead = new ListNode(0);
    ListNode pointer = dummyHead;
    Heap<ListNode> minHeap = new Heap<ListNode>();

    for(int i = 0; i < lists.length; i++) {
      minHeap.insert(lists[0]);
    }

    while(minHeap.size() > 0) {
      ListNode min = minHeap.deleteMin();
      pointer.next = min;
      if(min.next != null) {
        minHeap.insert(min.next);
      }
      pointer = pointer.next;
    }

    return dummyHead.next;
  }

  /*
  Use java.util.PriorityQueue
   */

  static Comparator<ListNode> ListNodeComparator = new Comparator<ListNode>() {
    @Override
    public int compare(ListNode a, ListNode b) {
      return a.val - b.val;
    }
  };

  public ListNode mergeKListsWithPriorityQueue(ListNode[] lists) {
    if (lists.length == 0) {
      return null;
    }

    ListNode dummyHead = new ListNode(0);
    ListNode pointer = dummyHead;
    Queue<ListNode> minHeap = new PriorityQueue<>(lists.length, MergeKSortedLinkedLists.ListNodeComparator);

    for (int i = 0; i < lists.length; i++) {
      if (lists[i] != null) {
        minHeap.add(lists[i])
      }
    }

    while(minHeap.size() > 0) {
      ListNode min = minHeap.poll();
      pointer.next = min;
      pointer = pointer.next;
      if (min.next != null) {
        minHeap.add(min.next);
      }
    }

    return dummyHead.next;
  }

  /*
  Divide and conquer
  Merge every two lists;
   */

  public ListNode mergeKListsByMergeEachTwoLists(List<ListNode> lists) {
    if(lists.isEmpty()) return null;

    int end = lists.size() - 1;

    while(end > 0){
      int begin = 0;
      while(end > begin) {
        lists.set(begin, merge2Lists(lists.get(begin), lists.get(end)));
        begin++;
        end--;
      }
    }

    return lists.get(0);
  }

  private ListNode merge2Lists(ListNode l1, ListNode l2) {
    ListNode dummyHead = new ListNode(0);
    ListNode pointer = dummyHead;
    while(l1 != null && l2 != null) {
      if(l1.val < l2.val) {
        pointer.next = l1;
        l1 = l1.next;
      } else {
        pointer.next = l2;
        l2 = l2.next;
      }
      pointer = pointer.next;
    }

    if(l1 != null) {
      pointer.next = l1;
    }

    if(l2 != null) {
      pointer.next = l2;
    }

    return dummyHead.next;
  }
}

package javasolutions.p138;

import javasolutions.RandomListNode;
import java.util.Map;
import java.util.HashMap;

public class CopyListWithRandomPointer {
  public RandomListNode copyRandomList(RandomListNode head) {
    if(head == null) return null;

    Map<RandomListNode, RandomListNode> oldToNewMapping = new HashMap<>();
    RandomListNode dummyHead = new RandomListNode(0);
    RandomListNode copyPointer = dummyHead;
    RandomListNode originalPointer = head;

    while(originalPointer != null) {
      copyPointer.next = new RandomListNode(originalPointer.label);
      oldToNewMapping.put(originalPointer, copyPointer.next);
      originalPointer = originalPointer.next;
      copyPointer = copyPointer.next;
    }

    originalPointer = head;
    copyPointer = dummyHead.next;

    while(originalPointer != null) {
      if(originalPointer.random != null) {
        copyPointer.random = oldToNewMapping.get(originalPointer.random);
      }
      originalPointer = originalPointer.next;
      copyPointer = copyPointer.next;
    }

    return dummyHead.next;
  }

  // Manipulate the original list and restore it
  // Insert the copied node after the original node
  public RandomListNode copyRandomListBetter(RandomListNode head) {
    if(head == null) return null;

    // Insert the copied node after the original node
    RandomListNode original = head;
    while(original != null) {
      RandomListNode copy = new RandomListNode(original.label);

      RandomListNode nextInOriginal = original.next;
      copy.next = nextInOriginal;
      original.next = copy;

      original = nextInOriginal;
    }

    // Assign all the random pointer for copied nodes
    original = head;
    while(original != null) {
      RandomListNode copy = original.next;
      copy.random = original.random == null ? null : original.random.next;
      original = original.next.next;
    }

    original = head;
    RandomListNode copyHead = original.next;

    // Restore original
    while(original != null) {
      RandomListNode copy = original.next;
      original.next = copy.next;
      copy.next = copy.next == null ? null : copy.next.next;
      original = original.next;
    }

    return copyHead;
  }
}
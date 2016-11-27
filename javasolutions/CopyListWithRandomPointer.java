package javasolutions;

import java.util.Map;
import java.util.HashMap;

public class CopyListWithRandomPointer {

	/**
	 * Use Map
	 * 	key: the node position in original list
	 * 	value: the node position in the new copy list
	 * 	Given the node.random, we can retrieve the new position and assignt to
	 * 	the new node
	 * @param  head [description]
	 * @return      [description]
	 */
	public RandomListNode copyRandomList(RandomListNode head) {
		if(head == null) return null;

		Map<RandomListNode, RandomListNode> map = new HashMap<>();
		RandomListNode dummyHead = new RandomListNode(0);
		RandomListNode pointerForOrigin = head;
		RandomListNode pointerForCopy = dummyHead;

		while (pointerForOrigin != null) {
			pointerForCopy.next = new RandomListNode(pointerForOrigin.label);
			map.put(pointerForOrigin, pointerForCopy.next);
			pointerForCopy = pointerForCopy.next;
			pointerForOrigin = pointerForOrigin.next;
		}

		pointerForOrigin = head;
		pointerForCopy = dummyHead.next;

		while(pointerForOrigin != null) {
			pointerForCopy.random = map.get(pointerForOrigin.random);
			pointerForOrigin = pointerForOrigin.next;
			pointerForCopy = pointerForCopy.next;
		}

		return dummyHead.next;
	}


// To summarize, we need three iterations over the list:
// i. Create a copy of each of the original node and insert them in
// 		between two original nodes in an alternate fashion.
// ii. Assign random pointer of each node copy.
// iii. Restore the input to its original configuration.
	public RandomListNode copyRandomListWithoutMap(RandomListNode head) {
		if(head == null) return null;

		RandomListNode pointer = head;
		while(pointer != null) {
			RandomListNode nextNodeInOrigin = pointer.next;
			RandomListNode copy = new RandomListNode(pointer.label);
			pointer.next = copy;
			copy.next = nextNodeInOrigin;
			pointer = nextNodeInOrigin;
		}

		pointer = head;
		while(pointer != null) {
			RandomListNode copy = pointer.next;
			copy.random = pointer.random == null ? null : pointer.random.next;
			pointer = pointer.next.next;
		}

		pointer = head;
		RandomListNode headCopy = pointer == null ? null : pointer.next;
		while (pointer != null) {
			RandomListNode copy = pointer.next;
			pointer.next = copy.next;
			pointer = pointer.next;
			copy.next = pointer == null ? null : pointer.next;
		}
		return headCopy;
	}
}
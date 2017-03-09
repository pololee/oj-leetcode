/**
 * https://leetcode.com/problems/linked-list-random-node/?tab=Description
 *
 * https://www.wikiwand.com/en/Reservoir_sampling
 */

package javasolutions.p382;

import javasolutions.ListNode;
import java.util.Random;

public class LinkedListRandomNode {
  private ListNode head;

  public LinkedListRandomNode(ListNode head) {
    this.head = head;
  }

  public int getRandom() {
    ListNode current = head;
    int answer = head.val;

    for (int i = 1; current.next != null; i++) {
      current = current.next;

      if (random(i) == 0) {
        answer = current.val;
      }
    }

    return answer;
  }

  // generate a random number between 0 and i (both inclusive)
  // Check java java.util.Random
  private int random(int i) {
    Random rand = new Random();
    return rand.nextInt(i + 1);
  }
}
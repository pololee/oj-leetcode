package javasolutions;

public class ListNode implements Comparable<ListNode> {
  int val;
  ListNode next;

  ListNode(int x) {
    val = x;
  }

  public int compareTo(ListNode other) {
    return (this.val - other.val);
  }
}

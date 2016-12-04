package javasolutions;

public class ListNode implements Comparable<ListNode> {
  public int val;
  public ListNode next;

  public ListNode(int x) {
    val = x;
  }

  public int compareTo(ListNode other) {
    return (this.val - other.val);
  }
}

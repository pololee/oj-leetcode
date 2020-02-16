package javasolutions;

public class ListNodeTest {
  public static void main(String[] args) {
    ListNode a = new ListNode(5);
    ListNode b = new ListNode(6);

    System.out.println(a.compareTo(b));
    System.out.println(b.compareTo(a));
  }
}
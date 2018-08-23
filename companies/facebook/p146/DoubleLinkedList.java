package facebook.p146;

import java.util.HashMap;

public class DoubleLinkedList {
  static class Node {
    int value;
    Node pre;
    Node next;

    public Node(int value) {
      this.value = value;
      pre = null;
      next = null;
    }
  }

  Node head = null;
  Node end = null;
  HashMap<Integer, Node> map = new HashMap<>();

  public void add(int value) {
    Node node = new Node(value);
    map.put(value, node);

    if (head == null) {
      head = node;
      end = node;
    } else {
      end.next = node;
      node.pre = end;
      end = node;
    }
  }

  public void remove(int value) {
    if (map.containsKey(value)) {
      Node n = map.get(value);

      if (n.pre != null) {
        n.pre.next = n.next;
      } else {
        head = n.next;
      }

      if (n.next != null) {
        n.next.pre = n.pre;
      } else {
        end = n.pre;
      }
    }
  }

  public void print() {
    Node point = head;
    while(point != null) {
      System.out.println(point.value);
      point = point.next;
    }
  }

  public static void main(String[] args) {
    DoubleLinkedList list = new DoubleLinkedList();
    list.add(1);
    list.add(2);
    list.add(3);
    list.print();
    list.remove(4);
    list.print();
  }
}
package javasolutions.p381;

import java.util.Collections;
import java.util.PriorityQueue;

public class PlayPriorityQueue {
  public static void natualOrder() {
    PriorityQueue<Integer> queue = new PriorityQueue<>();
    queue.add(1);
    queue.add(10);
    queue.add(5);
    queue.add(8);

    System.out.println(queue.poll());

    queue.add(7);
    System.out.println(queue.poll());
    System.out.println(queue.poll());
    System.out.println(queue.poll());
    System.out.println(queue.poll());
  }

  public static void reverseOrder() {
    PriorityQueue<Integer> queue = new PriorityQueue<>(10, Collections.reverseOrder());
    queue.add(1);
    queue.add(10);
    queue.add(5);
    queue.add(8);

    System.out.println(queue.poll());

    queue.add(7);
    System.out.println(queue.poll());
    System.out.println(queue.poll());
    System.out.println(queue.poll());
    System.out.println(queue.poll());
  }

  public static void main(String[] args) {
    PlayPriorityQueue.natualOrder();
    PlayPriorityQueue.reverseOrder();
  }
}
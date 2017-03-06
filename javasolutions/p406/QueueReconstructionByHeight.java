/**
 * https://leetcode.com/problems/queue-reconstruction-by-height/?tab=Description
 * http://www.baeldung.com/java-8-sort-lambda
 * http://stackoverflow.com/questions/322715/when-to-use-linkedlist-over-arraylist
 */

package javasolutions.p406;

import java.util.Arrays;
import java.util.List;
import java.util.LinkedList;

public class QueueReconstructionByHeight {
  public int[][] reconstructQueue(int[][] people) {
    /**
     * Pick up the tallest guys first
     * When insert the next tall guy, just need to insert him into k-th position
     * Repeat it until all people are inserted into the list
     */

    // Sort people, taller people first, if same height, smaller k value first
    Arrays.sort(people, (a, b) -> a[0] != b[0] ?  b[0] - a[0] : a[1] - b[1]);

    List<int[]> result = new LinkedList<>();
    for (int[] person : people) {
      result.add(person[1], person);
    }

    return result.toArray(new int[0][0]);
  }

  public void print(int[][] input) {
    for (int i = 0; i < input.length; i++) {
      System.out.format("(%d, %d)", input[i][0], input[i][1]);

      if (i != input.length - 1) {
        System.out.print(", ");
      }
    }

    System.out.println();
  }

  public static void main(String[] args) {
    int[][] test = { {7, 0}, {4, 4}, {7, 1}, {5, 0}, {6, 1}, {5, 2} };

    QueueReconstructionByHeight cal = new QueueReconstructionByHeight();

    System.out.println("Init array:");
    cal.print(test);

    int[][] answer = cal.reconstructQueue(test);

    System.out.println("After sorted:");
    cal.print(test);

    System.out.println("Answer:");
    cal.print(answer);
  }
}
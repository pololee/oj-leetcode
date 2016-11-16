/**
 * Given a number represented as an array of digits, plus one to the number.
 *
 * Could the number be negative?
 * No. Assume it is a non-negative number.
 *
 * How are the digits ordered in the list?
 * For example, is the number 12 represented by [1,2] or [2,1]?
 * The digits are stored such that the most significant digit is at the head of the list.
 *
 * Could the number contain leading zeros, such as [0,0,1]?
 * No
 */

import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;

public class PlusOne {
  public void plusOne(List<Integer> input) {
    for (int i = input.size() - 1; i >= 0; i--) {
      int current = input.get(i);
      if (current < 9) {
        input.set(i, current + 1);
        return;
      } else {
        input.set(i, 0);
      }
    }

    input.add(0);
    input.set(0, 1);
  }

  public static void main(String[] args) {
    PlusOne adder = new PlusOne();
    List<Integer> test1 = new ArrayList<Integer>(Arrays.asList(1, 3, 9));

    List<Integer> test2 = new ArrayList<Integer>(Arrays.asList(9, 9, 9));
    
    adder.plusOne(test1);
    adder.plusOne(test2);

    System.out.println(Arrays.toString(test1.toArray()));
    System.out.println(Arrays.toString(test2.toArray()));
  }
}

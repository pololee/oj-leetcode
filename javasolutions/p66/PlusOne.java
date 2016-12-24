package javasolutions.p66;

import java.util.Arrays;

public class PlusOne {
  public int[] plusOne(int[] digits) {
    if(digits.length == 0) return null;

    int addOne = 1, sum = 0;
    for(int i=digits.length-1; i>=0; i--) {
      sum = digits[i] + addOne;
      digits[i] = sum % 10;
      addOne = sum / 10;
    }

    if(addOne > 0) {
      int[] result = new int[digits.length+1];
      result[0] = 1;

      for(int i=0; i<digits.length; i++) {
        result[i+1] = digits[i];
      }

      return result;
    } else {
      return digits;
    }
  }

  public static void main(String[] args) {
    int[] test = {1, 2, 3};
    int[] test2 = {9, 9, 9};

    PlusOne cal = new PlusOne();

    System.out.println(Arrays.toString(cal.plusOne(test)));
    System.out.println(Arrays.toString(cal.plusOne(test2)));
  }
}
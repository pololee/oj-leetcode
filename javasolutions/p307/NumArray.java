package javasolutions.p307;

public class NumArray {
  private int[] inputArray;
  private int[] BIT;

  public NumArray(int[] nums) {
    inputArray = nums;
    int length = inputArray.length;
    BIT = new int[length+1];

    for (int i=0; i<length; i++) {
      updateBIT(i, inputArray[i]);
    }
  }

  void update(int i, int val) {
    updateBIT(i, val - inputArray[i]);

    inputArray[i] = val;
  }

  public int sumRange(int i, int j) {
    int sumJ = sumUptoInclusive(j);
    int sumIminusOne = sumUptoInclusive(i-1);

    return sumJ - sumIminusOne;
  }

  private void updateBIT(int i, int delta) {
    int index = i + 1;

    while(index <= inputArray.length) {
      BIT[index] += delta;
      index += lastSetBit(index);
    }
  }

  private int sumUptoInclusive(int i) {
    int index = i + 1;
    int answer = 0;

    while(index != 0) {
      answer += BIT[index];
      index -= lastSetBit(index);
    }

    return answer;
  }

  private int lastSetBit(int x) {
    return x & (-x);
  }

  public static void main(String[] args) {
    int[] test = {1, 3, 5};

    NumArray cal = new NumArray(test);
    System.out.println(cal.sumRange(0, 2));
    cal.update(1, 2);
    System.out.println(cal.sumRange(0, 2));
  }
}
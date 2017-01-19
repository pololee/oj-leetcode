package javasolutions.learn;

public class BinaryIndexedTree {
  private int[] BIT;
  private int inputArrayLength;

  public BinaryIndexedTree(int[] inputArray) {
    inputArrayLength = inputArray.length;
    BIT = new int[inputArrayLength + 1];

    for (int i=0; i<inputArrayLength; i++) {
      update(i, inputArray[i]);
    }
  }

  public void update(int idx, int delta) {
    int index = idx + 1;

    while(index <= inputArrayLength) {
      BIT[index] += delta;
      index += lastSetBit(index);
    }
  }

  public int sumUpToInclusive(int idx) {
    int index = idx + 1;
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

  public void printBIT() {
    for (int i=0; i<inputArrayLength; i++) {
      System.out.format("%d, ", BIT[i+1]);
    }

    System.out.println();
  }

  public static void main(String[] args) {
    int[] test = {5, 1, 15, 11, 52, 28, 0};
    BinaryIndexedTree cal = new BinaryIndexedTree(test);
    cal.printBIT();
    System.out.println(cal.sumUpToInclusive(2));

    cal.update(0, 5);
    cal.printBIT();
  }
}

/**
 * Tutorial:
 * 1. http://cs.stackexchange.com/questions/10538/bit-what-is-the-intuition-behind-a-binary-indexed-tree-and-how-was-it-thought-a
 * 2. https://www.hackerearth.com/practice/notes/binary-indexed-tree-or-fenwick-tree/
 * 3. http://theoryofprogramming.com/2014/12/24/binary-indexed-tree-or-fenwick-tree/
 */
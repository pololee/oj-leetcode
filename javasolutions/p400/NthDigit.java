package javasolutions.p400;

public class NthDigit {
  public int findNthDigit(int n) {
    int length = 1, start = 1;
    long count = 9;

    while(n > length * count) {
      n -= length * count;

      length++;
      count *= 10;
      start *= 10;
    }

    start += (n-1)/length;
    String str = String.valueOf(start);

    return Character.getNumericValue(str.charAt((n-1)%length));
  }

  public static void main(String[] args) {
    NthDigit cal = new NthDigit();
    System.out.println(cal.findNthDigit(12));
  }
}
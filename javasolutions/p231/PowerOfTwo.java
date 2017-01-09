package javasolutions.p231;

// The key is to think how an integer is represented in binary format
// 1 1
// 2 10
// 4 100
// 8 1000
// 16 10000

public class PowerOfTwo {
  public boolean isPowerOfTwo(int n) {
    int count = 0;

    while(n > 0){
      count += (n & 1);
      n = n >> 1;
    }

    return count == 1;
  }

  public boolean isPowerOfTwoBest(int n) {
    return n > 0 && (n & (n - 1)) == 0;
  }
}
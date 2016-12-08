package javasolutions.learn;

public class Fibonacci {
  public static int fibonacci(int i) {
    if(i == 0) return 0;
    if(i == 1) return 1;
    return fibonacci(i - 1) + fibonacci(i - 2);
  }

  public static void main(String[] args) {
    int n = 6;
    System.out.println(Fibonacci.fibonacci(n));
  }
}
package javasolutions.learn;

public class Fibonacci {
  public static int fibonacci(int i) {
    if(i == 0) return 0;
    if(i == 1) return 1;
    return fibonacci(i - 1) + fibonacci(i - 2);
  }

  public static int fibonacciTopDown(int i) {
    int[] memo = new int[i+1];
    return fibonacciTopDownHelper(i, memo);
  }

  private static int fibonacciTopDownHelper(int i, int[] memorized) {
    if(i == 0) return 0;
    if(i == 1) return 1;

    if (memorized[i] == 0) {
      memorized[i] = fibonacciTopDownHelper(i-1, memorized) + fibonacciTopDownHelper(i-2, memorized);
    }

    return memorized[i];
  }

  public static int fibonacciBottomUp(int i) {
    if(i == 0) return 0;
    if(i == 1) return 1;

    int[] memo = new int[i+1];
    memo[0] = 0;
    memo[1] = 1;

    for (int x = 2; x <= i; x++) {
      memo[x] = memo[x-1] + memo[x-2];
    }

    return memo[i];
  }

  public static int fibonacciBottomUp2(int i) {
    if(i == 0) return 0;
    if(i == 1) return 1;

    int fib_n_minus_2 = 0;
    int fib_n_minus_1 = 1;
    int fib_n = 0;

    for (int x = 2; x <= i; x++) {
      fib_n = fib_n_minus_1 + fib_n_minus_2;
      fib_n_minus_2 = fib_n_minus_1;
      fib_n_minus_1 = fib_n;
    }

    return fib_n;
  }

  public static void main(String[] args) {
    int n = 6;
    System.out.println(Fibonacci.fibonacci(n));
    System.out.println(Fibonacci.fibonacciTopDown(n));
    System.out.println(Fibonacci.fibonacciBottomUp(n));
    System.out.println(Fibonacci.fibonacciBottomUp2(n));
  }
}
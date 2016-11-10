import java.util.Arrays;

public class TwoSumII {
  public static int[] findTwoSumII(int[] sortedArry, int sum){
    int low = 0;
    int high = sortedArry.length - 1;

    while(low < high) {
      if (sortedArry[low] + sortedArry[high] > sum) {
        high--;
      } else if (sortedArry[low] + sortedArry[high] < sum) {
        low++;
      } else {
        return new int[]{low + 1, high + 1};
      }
    }

    throw new IllegalArgumentException("No two sum solution.");
  }

  public static void main(String[] arys) {
    int[] test = {1, 2, 3, 5};
    int sum = 5;

    System.out.println(Arrays.toString(TwoSumII.findTwoSumII(test, sum)));
  }
}

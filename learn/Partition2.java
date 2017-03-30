import java.util.Arrays;

public class Partition2 {
  private static void swap(int[] nums, int a, int b) {
    if(a == b) return;

    int temp = nums[a];
    nums[a] = nums[b];
    nums[b] = temp;
  }

  public static int partition(int[] nums, int left, int right, int pivotIndex) {
    int pivotValue = nums[pivotIndex];
    
    /**
    swap pivot with first element.
    then pivot final postion will be rightMark
     */
    swap(nums, left, pivotIndex);

    int leftMark = left + 1;
    int rightMark = right;

    while(true) {

      while(leftMark <= rightMark && nums[leftMark] <= pivotValue) {
        leftMark++;
      }

      while(rightMark >= leftMark && nums[rightMark] >= pivotValue) {
        rightMark--;
      }

      if(rightMark < leftMark) {
        break;
      } else {
        swap(nums, leftMark, rightMark);
      }
    }

    swap(nums, left, rightMark);
    return rightMark;
  }

  public static void main(String[] args) {
    int[] test = {1, 2, 3, 5, 6, 7, 4};

    System.out.println(Arrays.toString(test));
    int index = partition(test, 0, 6, 6);
    System.out.println("pivot final index:" + index);
    System.out.println(Arrays.toString(test));
  }
}
import java.util.Arrays;

public class Partition {
  public static int partition(int[] nums, int left, int right, int pivotIndex) {
    int pivotValue = nums[pivotIndex];

    /**
    swap the pivot with the end element
    Then the final pivot postion will be "leftMark"
     */
    swap(nums, right, pivotIndex);

    int leftMark = left;
    int rightMark = right - 1;
    
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
        swap(nums, rightMark, leftMark);
      }
    }

    swap(nums, leftMark, right);
    return leftMark;
  }

  private static void swap(int[] nums, int a, int b) {
    if(a == b) return;

    int temp = nums[a];
    nums[a] = nums[b];
    nums[b] = temp;
  }

  public static void main(String[] args) {
    int[] test = {1, 2, 3, 5, 6, 7, 4};

    System.out.println(Arrays.toString(test));
    int index = partition(test, 0, 6, 6);
    System.out.println("pivot final index:" + index);
    System.out.println(Arrays.toString(test));
  }
}
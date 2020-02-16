package javasolutions.p153;

public class FindMinInRotatedSortedArray {
  public int findMin(int[] nums) {
    int low = 0, high = nums.length - 1;

    while(low < high && nums[low] >= nums[high]) {
      int middle = (low+high)/2;

      if(nums[middle] > nums[high]) {
        low = middle + 1;
      } else {
        high = middle;
      }
    }

    return nums[low];
  }

  public static void main(String[] args) {
    int[] test = {4, 5, 6, 7, 0, 1, 2};

    FindMinInRotatedSortedArray cal = new FindMinInRotatedSortedArray();
    System.out.println(cal.findMin(test));
  }
}
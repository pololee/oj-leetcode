package javasolutions.p154;


// Corner case: For case where AL == AM == AR, the minimum could be on AM’s left or right side 
// (eg, [1, 1, 1, 0, 1] or [1, 0, 1, 1, 1]). In this case, 
// we could not discard either subarrays and therefore such worst case degenerates to the order of O(n).
public class FindMinInRotatedSortedArrayII {
  public int findMin(int[] nums) {
    int low = 0, high = nums.length - 1;
    int middle = 0;

    while(low < high && nums[low] >= nums[high]) {
      middle = low + (high - low) / 2;

      if(nums[middle] > nums[high]) {
        low = middle + 1;
      } else if(nums[middle] < nums[low]) {
        high = middle;
      } else {
        low = low + 1;
      }
    }

    return nums[low];
  }

  public static void main(String[] args) {
    int[] test = {1, 1, 1, 0, 1};

    FindMinInRotatedSortedArrayII cal = new FindMinInRotatedSortedArrayII();
    System.out.println(cal.findMin(test));
  }
}
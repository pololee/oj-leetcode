package javasolutions.p35;

public class SearchInsertPosition {
  public int searchInsert(int[] nums, int target) {
    int length = nums.length;

    int low = 0, high = length - 1;
    int middle = 0, current = 0, insertPosition = 0;

    while(low <= high) {
      middle = (low + high) / 2;
      current = nums[middle];

      if(target == current) {
        return middle;
      } else if(target > current) {
        low = middle + 1;
        insertPosition = low;
      } else {
        high = middle - 1;
        insertPosition = high >= 0 ? high : 0;
      }
    }

    return insertPosition;
  }

  public int searchInsert2(int[] nums, int target) {
    int low = 0, high = nums.length - 1;

    while(low < high) {
      int middle = (low + high) / 2;
      
      if(target > nums[middle]) {
        low = middle + 1;
      } else {
        high = middle;
      }
    }

    return (nums[low] < target) ? low + 1 : low;
  }

  public static void main(String[] args) {
    int[] test = {1,3,5,6};
    SearchInsertPosition cal = new SearchInsertPosition();

    System.out.println(cal.searchInsert(test, 5));
    System.out.println(cal.searchInsert(test, 2));
    System.out.println(cal.searchInsert(test, 7));
    System.out.println(cal.searchInsert(test, 0));

    System.out.println(cal.searchInsert2(test, 5));
    System.out.println(cal.searchInsert2(test, 2));
    System.out.println(cal.searchInsert2(test, 7));
    System.out.println(cal.searchInsert2(test, 0));
  }
}
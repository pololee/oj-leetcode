package javasolutions.binarySearch;

public class Basic {
  public int binarySearch(int[] nums, int target) {
    int low = 0, high = nums.length - 1;

    int middle = 0;
    while(low <= high) {
      middle = (low + high) / 2;
      
      if(nums[middle] == target) {
        return middle;
      } else if (target > nums[middle]) {
        low = middle + 1;
      } else {
        high = middle - 1;
      }
    }

    return -1;
  }

  // http://canhazcode.blogspot.com/2012/02/we-need-to-talk-about-binary-search.html
  // Lower-bound search: finding the minium index with the target value
  private boolean lowerBoundPredicate(int element, int target) {
    return element >= target;
  }

  public int lowerBoundSearch(int[] nums, int target) {
    int low = 0, high = nums.length - 1;
    int bestSoFar = 0;

    while(low < high) {
      int middle = low + (high - low) / 2;

      if(lowerBoundPredicate(nums[middle], target)) {
        bestSoFar = middle;
        high = middle - 1;
      } else {
        low = middle + 1;
      }
    }

    return bestSoFar;
  }

  // upper-bound search: finding the maximum index with the target value
  private boolean upperBoundPredicate(int element, int target) {
    return element <= target;
  }

  public int upperBoundSearch(int[] nums, int target){
    int low = 0, high = nums.length - 1;
    int bestSoFar = 0;

    while(low < high) {
      int middle = low + (high - low) / 2;

      if(upperBoundPredicate(nums[middle], target)) {
        bestSoFar = middle;
        low = middle + 1;
      } else {
        high = middle - 1;
      }
    }

    return bestSoFar;
  }

  public static void main(String[] args) {
    int[] test = {0, 5, 13, 19, 22, 41, 55, 68, 72, 81, 98};

    Basic cal = new Basic();
    System.out.println(cal.binarySearch(test, 55));
    System.out.println(cal.binarySearch(test, 100));

    int[] test2 = {1, 1, 2, 4, 5, 5, 5, 6, 6, 6, 6, 8, 10, 10, 11};
    System.out.println(cal.lowerBoundSearch(test2, 6));
    System.out.println(cal.upperBoundSearch(test2, 6));
  }
}
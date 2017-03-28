/**
http://interactivepython.org/courselib/static/pythonds/SortSearch/TheQuickSort.html

use divide and conquer to gain the same advantage as merge sort,
while not using additional space

At the point where rightmark becomes less than leftmark, we stop. 
The position of rightmark is now the split point.

To analyze the quickSort function, note that for a list of length n, 
if the partition always occurs in the middle of the list, 
there will again be lognlog⁡n divisions. 
In order to find the split point, 
each of the n items needs to be checked against the pivot value. 
The result is nlognnlog⁡n. In addition, 
there is no need for additional memory as in the merge sort process.

Unfortunately, in the worst case, 
the split points may not be in the middle and can be very skewed to the left or the right, 
leaving a very uneven division. In this case, 
sorting a list of n items divides into sorting a list of 0 items and a list of n−1 items. 
Then sorting a list of n−1 divides into a list of size 0 and a list of size n−2, and so on. 
The result is an O(n^2) sort with all of the overhead that recursion requires.

We mentioned earlier that there are different ways to choose the pivot value. 
In particular, we can attempt to alleviate some of the potential for an uneven division 
by using a technique called median of three. To choose the pivot value, 
we will consider the first, the middle, and the last element in the list. 
In our example, those are 54, 77, and 20. Now pick the median value, in our case 54, 
and use it for the pivot value (of course, that was the pivot value we used originally). 
The idea is that in the case where the the first item in the list does not belong 
toward the middle of the list, the median of three will choose a better “middle” value. 
This will be particularly useful when the original list is somewhat sorted to begin with. 

 */

import java.util.Arrays;

public class QuickSort {
  public static void sort(int[] nums) {
    sortHelper(nums, 0, nums.length - 1);
  }

  private static void sortHelper(int[] nums, int first, int last) {
    if(first < last) {
      int splitPoint = partition(nums, first, last);

      System.out.println("Found splitPoint: " + splitPoint);
      System.out.println(Arrays.toString(nums));

      sortHelper(nums, first, splitPoint - 1);
      sortHelper(nums, splitPoint + 1, last);
    }
  }

  private static int partition(int[] nums, int first, int last) {
    int pivotValue = nums[first];

    int leftMark = first + 1;
    int rightMark = last;

    boolean done = false;
    while(!done) {

      while(leftMark <= rightMark && nums[leftMark] <= pivotValue) {
        leftMark++;
      }

      while(leftMark <= rightMark && nums[rightMark] >= pivotValue) {
        rightMark--;
      }

      if(rightMark < leftMark) {
        done = true;
      } else {
        int temp = nums[rightMark];
        nums[rightMark] = nums[leftMark];
        nums[leftMark] = temp;
      }
    }

    nums[first] = nums[rightMark];
    nums[rightMark] = pivotValue;

    return rightMark;
  }

  public static void main(String[] args) {
    int[] test = {54,26,93,17,77,31,44,55,20};

    QuickSort.sort(test);
  }
}
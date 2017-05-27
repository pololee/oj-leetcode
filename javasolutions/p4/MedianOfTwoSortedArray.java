/**
https://leetcode.com/problems/median-of-two-sorted-arrays/#/description

The best explanation I found
https://kartikkukreja.wordpress.com/2016/10/13/problem-of-the-day-median-of-two-sorted-arrays/

Input:
A = [1,3,5]
B = [4,7]

Assume 1-based indexing for simplification.

Step 1:
N = 3, M = 2, k = (3+2)/2 + 1 = 3
pa = 3/2 = 1, pb = 3-1 = 2
A[1] = 1 <= B[2] = 7
Continue search for k-pa = 3-1 = 2nd order statistic in A[2:] = [3,5] and B[:2] = [4,7].

Step 2:
A = [3,5], B = [4,7]
N = 2, M = 2, k = 2
pa = 2/2 = 1, pb = 2-1 = 1
A[1] = 3 <= B[1] = 4
Continue search for k-pa = 2-1 = 1st order statistic in A[2:] = [5] and B[:1] = [4].

Step 3:
A = [5], B = [4], k = 1
Since k == 1, return min(A[1], B[1]) = min(5,4) = 4.

4 is the median.
 */

package javasolutions.p4;

public class MedianOfTwoSortedArray {
  public double findMedianSortedArrays(int[] nums1, int[] nums2) {
    if(nums1 == null || nums2 == null || nums1.length == 0 && nums2.length == 0) {
        return 0.0;
    }
    
    int m = nums1.length;
    int n = nums2.length;
    int total = m + n;
    
    if(total % 2 != 0) {
        return findKth(nums1, 0, m - 1, nums2, 0, n - 1, total / 2 + 1);
    } else {
        double leftM = findKth(nums1, 0, m - 1, nums2, 0, n - 1, total / 2);
        double rightM = findKth(nums1, 0, m - 1, nums2, 0, n - 1, total / 2 + 1);
        
        return (leftM + rightM) / 2;
    }
  }

// Note: k is not index!!!
  private double findKth(int[] A, int startA, int endA, int[] B, int startB, int endB, int k) {
    int m = endA - startA + 1;
    int n = endB - startB + 1;
    
    /**
why this is important?

Take an example.
A = {1, 3, 5}, B = {4}, k = 3
Without this following if, partA = Math.min(3/2, 3) = 1. 
partB = 3 - 1 = 2, which cause index out of bound exception
 */
    if(m > n) {
        return findKth(B, startB, endB, A, startA, endA, k);
    }
    
    if(m == 0) {
        return B[startB + k - 1];
    }
    
    if(k == 1) {
        return Math.min(A[startA], B[startB]);
    }
    
    int partA = Math.min(k/2, m);
    int partB = k - partA;
    int midA = A[startA + partA - 1];
    int midB = B[startB + partB - 1];
    
    if(midA == midB) {
        return midA;
    } else if(midA < midB) {
        return findKth(A, startA + partA, endA, B, startB, startB + partB - 1, k-partA);
    } else {
        return findKth(A, startA, startA + partA - 1, B, startB + partB, endB, k-partB);
    }
  }

  public static void main(String[] args) {
    int[] A = {1, 3, 5};
    int[] B = {4};

    MedianOfTwoSortedArray cal = new MedianOfTwoSortedArray();
    System.out.println(cal.findMedianSortedArrays(A, B));
  }
}
/**
https://discuss.leetcode.com/topic/4996/share-my-o-log-min-m-n-solution-with-explanation

left_part          |        right_part
A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]

We need
1) len(left_part) == len(right_part)
2) max(left_part) <= min(right_part)

(1) i + j == m - i + n - j (or: m - i + n - j + 1)
    if n >= m, we just need to set: i = 0 ~ m, j = (m + n + 1)/2 - i
(2) B[j-1] <= A[i] and A[i-1] <= B[j]
 */

package javasolutions.p4;

public class Solution2 {
  public double findMedianSortedArrays(int[] nums1, int[] nums2) {
    if(nums1 == null || nums2 == null || nums1.length == 0 && nums2.length == 0) {
      return 0.0;
    }

    int[] A = nums1;
    int[] B = nums2;
    if(nums1.length > nums2.length) {
      A = nums2;
      B = nums1;
    }

    int m = A.length;
    int n = B.length;
    int total = m + n;

    int aMin = 0;
    int aMax = m;
    // halfTotal is actually half ( if total is even) or half+1
    // total = 5 => halfTotal = 3
    // total = 4 => halfTotal = 2
    // Because of this definition, the middle or leftMiddle value will be max(A[i-1], B[j-1])
    int halfTotal = (total + 1) / 2;
    
    while(aMin <= aMax) {
      int a = aMin + (aMax - aMin) / 2;
      int b = halfTotal - a;

      if(a < m && B[b-1] > A[a]) {
        aMin = a+1;
      } else if(a > 0 && A[a-1] > B[b]) {
        aMax = a - 1;
      } else {
        // i is perfect
        // A[i-1] <= B[j] && B[j-1] <= A[i]
        double maxOfLeft = 0.0;
        double minOfRight = 0.0;

        if(a == 0) {
          maxOfLeft = B[b-1];
        } else if(b == 0) {
          maxOfLeft = A[a-1];
        } else {
          maxOfLeft = Math.max(A[a-1], B[b-1]);
        }

        if(total % 2 != 0) {
          return maxOfLeft;
        }

        if(a == m) {
          minOfRight = B[b];
        } else if(b == n) {
          minOfRight = A[a];
        } else {
          minOfRight = Math.min(A[a], B[b]);
        }

        return (maxOfLeft + minOfRight) / 2;
      }
    }

    return 0.0;
  }

  public static void main(String[] args) {
    int[] A = {2, 9};
    int[] B = {1,3,4,5,6,7,8,10};

    Solution2 cal = new Solution2();
    System.out.println(cal.findMedianSortedArrays(A, B));
  }
}
/**
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/#/description
 */

package javasolutions.p378;

import java.util.PriorityQueue;
import java.util.Collections;

public class KthSmallestInSortedMatrix {
  public int kthSmallest(int[][] matrix, int k) {
    if(matrix.length == 0 || matrix[0].length == 0) return 0;
    PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());
    
    for(int row = 0; row < matrix.length; row++) {
        for(int col = 0; col < matrix[0].length; col++) {
            heap.add(matrix[row][col]);
            
            if(heap.size() > k) heap.poll();
        }
    }
    
    return heap.peek();
  }
}
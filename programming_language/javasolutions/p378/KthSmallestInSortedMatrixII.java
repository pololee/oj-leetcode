package javasolutions.p378;

import java.util.PriorityQueue;

public class KthSmallestInSortedMatrixII {

  static class Tuple implements Comparable<Tuple> {
    int row, col, val;
    
    public Tuple(int row, int col, int val) {
      this.row = row;
      this.col = col;
      this.val = val;
    }

    @Override
    public int compareTo(Tuple that) {
      return this.val - that.val;
    }
  }

  public int kthSmallest(int[][] matrix, int k) {
    if(matrix.length == 0 || matrix[0].length == 0) return 0;

    PriorityQueue<Tuple> queue = new PriorityQueue<Tuple>();
    int numOfRows = matrix.length;
    int bound = numOfRows > k ? k : numOfRows;

    // Insert the first row to the queue
    for(int i= 0; i < bound; i++) {
      queue.offer(new Tuple(0, i, matrix[0][i]));
    }

    for(int i = 0; i < k; i++) {
      Tuple current = queue.poll(); // retrieve and remove the smallest in the queue
      
      if(current.row < numOfRows - 1) {
        Tuple nextEleInTheCol = new Tuple(current.row + 1, current.col, matrix[current.row + 1][current.col]);
        queue.offer(nextEleInTheCol);
      }
    }

    return queue.poll().val;
  }

  public static void main(String[] args) {
    int[][] test = {{1, 5, 9}, {10, 11, 13}, {12, 13, 15}};

    KthSmallestInSortedMatrixII cal = new KthSmallestInSortedMatrixII();
    System.out.println(cal.kthSmallest(test, 7));
  }
}
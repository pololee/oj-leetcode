import java.io.*;
import java.util.*;


public class Test{
    public static void main(String args[]) throws Exception{
       Solution szy = new Solution();
       int[][] grid1 = {{1,1,1},{1,0,0},{1,0,0}};
       int[][] grid2 = {{1,1,1},{1,0,0},{1,0,1}};
       System.out.print(szy.ImageMatching(grid1, grid2));
       
     }
    
 }
class Solution {
 class Point{
  int x;
  int y;
  Point(int x, int y){
   this.x = x;
   this.y = y;
  }
 }
 int[] deltaX = {1,0,0,-1};
 int[] deltaY = {0,1,-1,0};
    public int ImageMatching(int[][] grid1, int[][] grid2) {
        if (grid1 == null || grid1.length == 0 || grid1[0].length == 0 || grid2 == null|| grid2.length == 0 || grid2[0].length == 0) {
         return 0;
        }
        
        int count = 0;
        
        int m1 = grid1.length;
        int n1 = grid1[0].length;
        int m2 = grid2.length;
        int n2 = grid2[0].length;
        
        for (int i = 0; i < m1; i++) {
         for (int j = 0; j < n1; j++) {
          if (grid1[i][j] == 1) {
           List<String> res1 = bfs (grid1, i,j, m1,n1);
           if (i < m2 && j < n2) {
            List<String> res2 = bfs (grid2, i,j, m2,n2);
            if (isEqual(res1,res2)) {
             count ++;
            }
           }
          }
         }
        }
        
        return count;
    }
    
    public List<String> bfs(int[][] grid, int i, int j ,int m, int n){
         List<String> res = new ArrayList<>();
          LinkedList<Point> queue = new LinkedList<>();
          grid[i][j] = 0;
          Point start = new Point(i,j);
          queue.add(start);
          
          while (!queue.isEmpty()) {
              Point k = queue.removeFirst();
              res.add(k.x + " " + k.y);
              for (int t = 0; t < 4; t++) {
                 Point next = new Point(k.x + deltaX[t], k.y + deltaY[t]);
                 if (next.x < 0 || next.x >= m || next.y < 0 || next.y >= n) {
                  continue;
                 }
                 
                 if (grid[next.x][next.y] == 0) {
                  continue;
                 }
                 
                 queue.add(next);
                 grid[next.x][next.y] = 0;
              }
          }
          
          return res;
    }
    
    public boolean isEqual(List<String> res1, List<String> res2) {
        if (res1.size() != res2.size()) {
         return false;
        }
        
        for (int i = 0; i < res1.size(); i++) {
         if (!res1.get(i).equals(res2.get(i))) {
          return false;
         }
        }
        
        return true;
    }
}
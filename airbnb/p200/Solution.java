/**
 * Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
 * An island is surrounded by water and is formed by connecting adjacent lands
 * horizontally or vertically.
 *
 * You may assume all four edges of the grid are all surrounded by water.
 */

package airbnb.p200;

public class Solution {
  private int numOfRows;
  private int numOfCols;

  public int numberOfIslands(char[][] grid) {
    if(grid.length == 0 || grid[0].length == 0) return 0;

    int count = 0;
    numOfRows = grid.length;
    numOfCols = grid[0].length;
    boolean[][] visited = new boolean[numOfRows][numOfCols];

    for(int i = 0; i < numOfRows; i++) {
      for(int j = 0; j < numOfCols; j++) {
        if(grid[i][j] == '1' && !visited[i][j]) {
          DFS(grid, visited, i, j);
          count++;
        }
      }
    }

    return count;
  }

  private void DFS(char[][] grid, boolean[][] visted, int row, int col) {
    if(row < 0 || row >= numOfRows) return;
    if(col < 0 || col >= numOfCols) return;
    if(grid[row][col] == '0' || visted[row][col]) return;

    visted[row][col] = true;

    DFS(grid, visted, row - 1, col);
    DFS(grid, visted, row + 1, col);
    DFS(grid, visted, row, col - 1);
    DFS(grid, visted, row, col + 1);
  }
}
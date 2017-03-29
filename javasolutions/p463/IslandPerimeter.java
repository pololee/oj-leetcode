package javasolutions.p463;

public class IslandPerimeter {
  public int perimeter(int[][] grid) {
    if(grid.length == 0 || grid[0].length == 0) return 0;

    int result = 0;
    for (int i=0; i<grid.length; i++) {
      for (int j=0; j<grid[0].length; j++) {
        if(grid[i][j] == 0) continue;

        result += 4;
        if(i > 0 && grid[i-1][j] == 1) result -=2; // the grid above is 1
        if(j > 0 && grid[i][j-1] == 1) result -=2; // the grid on the left is 1
      }
    }

    return result;
  }
}
import java.util.*;

public class Solution {
    /**
     * @param maze: the maze
     * @param start: the start
     * @param destination: the destination
     * @return: the shortest distance for the ball to stop at the destination
     */
    int[] dx = new int[] {1, 0, -1, 0};
    int[] dy = new int[] {0, 1, 0, -1};

    int shortestDist = Integer.MAX_VALUE;

    public int shortestDistance(int[][] maze, int[] start, int[] destination) {
        // write your code here
        int m = maze.length;
        int n = maze[0].length;
        
        boolean[][] visited = new boolean[m][n];
        dfsUtil(maze, visited, start[0], start[1], 0, destination);
        
        return shortestDist == Integer.MAX_VALUE ? -1 : shortestDist;
    }
    
    private void dfsUtil(int[][] maze, boolean[][] visited, int x, int y, int currDist, int[] destination) {
        if(x == destination[0] && y == destination[1]) {
            shortestDist = Math.min(shortestDist, currDist);
            return;
        }
        
        if(visited[x][y]) {
            return;
        }
        
        visited[x][y] = true;
        for(int i = 0; i < 4; i++) {
            int nx = x;
            int ny = y;
            int dist = currDist;
            
            while(!hitTheWall(maze, nx + dx[i], ny + dy[i])) {
                nx += dx[i];
                ny += dy[i];
                dist += 1;
            }
            
            dfsUtil(maze, visited, nx, ny, dist, destination);
        }
        
        visited[x][y] = false;
    }
    
    private boolean hitTheWall(int[][] maze, int x, int y) {
        int m = maze.length;
        int n = maze[0].length;
        
        if(x < 0 || x >= m || y < 0 || y >= n) {
            return true;
        }
        
        if(maze[x][y] == 1) return true;
        
        return false;
    }
}

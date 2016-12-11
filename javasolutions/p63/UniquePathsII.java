package javasolutions.p63;

public class UniquePathsII {
  public int uniquePathsWithObstacles(int[][] obstacleGrid) {
    if(obstacleGrid.length == 0) return 0;
    if(obstacleGrid[0][0] == 1) return 0;

    int numOfRows = obstacleGrid.length;
    int numOfCols = obstacleGrid[0].length;

    int[][] DP = new int[numOfRows][numOfCols];

    DP[0][0] = 1;
    for (int i=1; i<numOfRows; i++) {
      DP[i][0] = obstacleGrid[i][0] == 1 ? 0 : DP[i-1][0];
    }

    for (int i=1; i<numOfCols; i++) {
      DP[0][i] = obstacleGrid[0][i] == 1 ? 0 : DP[0][i-1];
    }

    for (int i=1; i<numOfRows; i++) {
      for (int j=1; j<numOfCols; j++) {
        if (obstacleGrid[i][j] == 1) {
          DP[i][j] = 0;
        } else {
          DP[i][j] = DP[i-1][j] + DP[i][j-1];
        }
      }
    }

    return DP[numOfRows-1][numOfCols-1];
  }

  public static void main(String[] args) {
    int[][] input = {
      {1, 0}
    };

    UniquePathsII cal = new UniquePathsII();
    System.out.println(cal.uniquePathsWithObstacles(input));
  }
}
package javasolutions.p62;

public class UniquePaths {
  public int uniquePaths(int m, int n) {
    if(m < 1 || n < 1) return 0;

    int[][] matrix = new int[m][n];
    matrix[0][0] = 1;
    return uniquePathsHelper(m - 1, n - 1, matrix);
  }

  private int uniquePathsHelper(int m, int n, int[][] matrix) {
    if(m < 0 || n < 0) return 0;
    if(m == 0 || n == 0) return 1;
    if(matrix[m][n] > 0) {
      return matrix[m][n];
    } else {
      matrix[m][n] = uniquePathsHelper(m - 1, n, matrix) + uniquePathsHelper(m, n - 1, matrix);
      return matrix[m][n];
    }
  }

  public int uniquePathsIterative(int m, int n) {
    if (m < 1 || n < 1) return 0;

    int[][] matrix = new int[m][n];

    for(int i=0; i<m; i++) {
      matrix[i][0] = 1;
    }

    for(int i=0; i<n; i++) {
      matrix[0][i] = 1;
    }

    for (int i = 1; i < m; i++) {
      for (int j = 1; j < n; j++) {
        matrix[i][j] = matrix[i-1][j] + matrix[i][j-1];
      }
    }

    return matrix[m-1][n-1];
  }

  public int uniquePathsIterative2(int m, int n) {
    if(m < 1 || n < 1) return 0;

    int[][] matrix = new int[m][n];
    matrix[0][0] = 1;

    int top = 0, left = 0;
    for(int i=0; i < m; i++) {
      for (int j=0; j<n; j++) {
        if(i == 0 && j == 0) continue;

        if(i == 0) {
          top = 0;
        } else {
          top = matrix[i-1][j];
        }

        if(j == 0) {
          left = 0;
        } else {
          left = matrix[i][j-1];
        }
        matrix[i][j] = top + left;
      }
    }

    return matrix[m-1][n-1];
  }

  // Use combinatorial solution,
  // the robot needs m-1 down and n-1 right to reach the target.(right-bottom)
  // So the total is m+n-2 steps. The solutions is to find m-1 down from m+n-2


  public static void main(String[] args) {
    UniquePaths cal = new UniquePaths();
    System.out.println(cal.uniquePaths(3, 3));
    System.out.println(cal.uniquePathsIterative(3, 3));
    System.out.println(cal.uniquePathsIterative2(3, 3));
  }
}
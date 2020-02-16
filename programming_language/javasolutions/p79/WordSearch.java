package javasolutions.p79;

public class WordSearch {
  public boolean exist(char[][] board, String word) {
    if (word.isEmpty()) return true;
    if (board.length == 0 || board[0].length == 0) return false;

    boolean[][] visited = new boolean[board.length][board[0].length];

    for (int i = 0; i < board.length; i++) {
      for (int j = 0; j < board[0].length; j++) {
        if (existDFS(board, visited, 0, word, i, j)) return true;
      }
    }

    return false;
  }

  private boolean existDFS(char[][] board, boolean[][] visited, int index, String word, int row, int col) {
    if (index == word.length()) return true;
    if (row < 0 || row >= board.length || col < 0 || col >= board[0].length || visited[row][col] || board[row][col] !=  word.charAt(index)) return false;

    visited[row][col] = true;
    boolean answer = existDFS(board, visited, index + 1, word, row - 1, col)
            || existDFS(board, visited, index + 1, word, row + 1, col)
            || existDFS(board, visited, index + 1, word, row, col - 1)
            || existDFS(board, visited, index + 1, word, row, col + 1);
    visited[row][col] = false;

    return answer;
  }
}
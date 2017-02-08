package javasolutions.p212;

import java.util.List;
import java.util.ArrayList;

public class WordSearchII {

  private class TrieNode {
    public String word;
    public TrieNode[] children;

    public TrieNode() {
      word = null;
      children = new TrieNode[26];
    }
  }

  private class Trie {
    public TrieNode root;

    public Trie() {
      root = new TrieNode();
    }

    void insert(String word) {
      TrieNode pointer = root;

      for (int i = 0; i < word.length(); i++) {
        int index = word.charAt(i) - 'a';

        if (pointer.children[index] == null) {
          pointer.children[index] = new TrieNode();
        }

        pointer = pointer.children[index];
      }

      pointer.word = new String(word);
    }
  }

  public List<String> findWords(char[][] board, String[] words) {
    List<String> foundWords = new ArrayList<>();

    if (board.length == 0 || board[0].length == 0 || words.length == 0) return foundWords;

    Trie trie = new Trie();
    for (int i = 0; i < words.length; i++) {
      trie.insert(words[i]);
    }

    TrieNode root = trie.root;
    boolean[][] visited = new boolean[board.length][board[0].length];

    for (int row = 0; row < board.length; row++) {
      for (int col = 0; col < board[0].length; col++) {
        int charIndex = board[row][col] - 'a';

        if (root.children[charIndex] != null) {
          findWordsHelper(board, row, col, root.children[charIndex], visited, foundWords);
        }
      }
    }

    return foundWords;
  }

  private static final int[][] MOVE_DIRECTIONS = {{ -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 }};

  private void findWordsHelper(char[][] board, int row, int col, TrieNode pointer, boolean[][] visited, List<String> foundWords) {
    if (pointer.word != null) {
      foundWords.add(pointer.word);
      pointer.word = null;
    }

    visited[row][col] = true;

    for (int i = 0; i < 4; i++) {
      int nextRow = row + MOVE_DIRECTIONS[i][0];
      int nextCol = col + MOVE_DIRECTIONS[i][1];

      if (nextRow >= 0
              && nextRow < board.length
              && nextCol >= 0
              && nextCol < board[0].length
              && !visited[nextRow][nextCol]
              && pointer.children[ board[nextRow][nextCol] - 'a' ] != null) {

        findWordsHelper(board, nextRow, nextCol, pointer.children[ board[nextRow][nextCol] - 'a' ], visited, foundWords);
      }
    }

    visited[row][col] = false;
  }

  public static void main(String[] args) {
    String[] words = {"oath","pea","eat","rain"};
    char[][] board = {
            { 'o','a','a','n' },
            { 'e','t','a','e' },
            { 'i','h','k','r' },
            { 'i','f','l','v' }
    };

    WordSearchII cal = new WordSearchII();

    List<String> answer = cal.findWords(board, words);
    for (String str : answer) {
      System.out.println(str);
    }
  }
}
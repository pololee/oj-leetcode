package javasolutions.p208;

public class Trie {
  private boolean isWord;
  private Trie[] children;

  public Trie() {
    isWord = false;
    children = new Trie[26];
  }

  public void insert(String word) {
    if (word.isEmpty()) {
      isWord = true;
      return;
    } else {
      int index = word.charAt(0) - 'a';

      if (children[index] == null) {
        children[index] = new Trie();
      }

      children[index].insert(word.substring(1, word.length()));
    }
  }

  public boolean search(String word) {
    if (word.isEmpty()) {
      return isWord;
    } else {
      int index = word.charAt(0) - 'a';

      if (children[index] == null) {
        return false;
      } else {
        return children[index].search(word.substring(1, word.length()));
      }
    }
  }

  public boolean startsWith(String prefix) {
    if (prefix.isEmpty()) {
      return true;
    } else {
      int index = prefix.charAt(0) - 'a';

      if (children[index] == null) {
        return false;
      } else {
        return children[index].startsWith(prefix.substring(1, prefix.length()));
      }
    }
  }
}
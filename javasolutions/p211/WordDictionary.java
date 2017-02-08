package javasolutions.p211;

public class WordDictionary {

  private class TrieNode {
    public boolean isWord;
    public TrieNode[] children;

    public TrieNode() {
      isWord = false;
      children = new TrieNode[26]; // a-z
    }
  }

  private TrieNode root;

  public WordDictionary() {
    root = new TrieNode();
  }

  public void addWord(String word) {
    TrieNode pointer = root;

    for (int i = 0; i < word.length(); i++) {
      int index = word.charAt(i) - 'a';

      if (pointer.children[index] == null) {
        pointer.children[index] = new TrieNode();
      }

      pointer = pointer.children[index];
    }

    pointer.isWord = true;
  }

  public boolean search(String word) {
    return searchDFS(word, 0, root);
  }

  private boolean searchDFS(String word, int index, TrieNode pointer) {
    if (index == word.length()) return pointer.isWord;

    if (word.charAt(index) == '.') {
      for (int i = 0; i < 26; i++) {
        if (pointer.children[i] != null && searchDFS(word, index + 1, pointer.children[i])) {
          return true;
        }
      }

      return false;
    } else {
      int charIndex = word.charAt(index) - 'a';
      return pointer.children[charIndex] != null && searchDFS(word, index + 1, pointer.children[charIndex]);
    }
  }

  public static void main(String[] args) {
    WordDictionary cal = new WordDictionary();

    cal.addWord("bad");
    cal.addWord("dad");
    cal.addWord("mad");
    System.out.println(cal.search("pad"));
    System.out.println(cal.search("bad"));
    System.out.println(cal.search(".ad"));
    System.out.println(cal.search("b.."));
  }
}
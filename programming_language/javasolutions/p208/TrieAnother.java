package javasolutions.p208;

public class TrieAnother {

  private class TrieNode {
    public boolean isWord;
    public TrieNode[] children;

    public TrieNode() {
      isWord = false;
      children = new TrieNode[26];
    }
  }

  private TrieNode root;

  public TrieAnother() {
    root = new TrieNode();
  }

  public void insert(String word) {
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
    if (word.isEmpty()) return true;

    TrieNode pointer = root;

    for (int i = 0; i < word.length(); i++) {
      int index = word.charAt(i) - 'a';

      if (pointer.children[index] == null) {
        return false;
      }

      pointer = pointer.children[index];
    }

    return pointer.isWord;
  }

  public boolean startsWith(String prefix) {
    if (prefix.isEmpty()) return true;

    TrieNode pointer = root;
    for (int i = 0; i < prefix.length(); i++) {
      int index = prefix.charAt(i) - 'a';

      if (pointer.children[index] == null) {
        return false;
      }

      pointer = pointer.children[index];
    }

    return true;
  }

  public static void main(String[] args) {
    TrieAnother obj = new TrieAnother();

    obj.insert("word");
    System.out.println(obj.search("word"));
    System.out.println(obj.startsWith("wor"));
  }

}
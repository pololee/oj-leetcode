package javasolutions.trie;

public class Trie {
  private boolean isWord;
  private Trie[] children;

  public Trie() {
    this.isWord = false;
    this.children = new Trie[26];
  }

  public boolean contains(String s) {
    if (s.isEmpty()) {
      return this.isWord;
    } else if ( !Character.isLowerCase(s.charAt(0)) ) {
      return false;
    } else if (this.children[ s.charAt(0) - 'a' ] == null) {
      return false;
    } else {
      return this.children[s.charAt(0) - 'a'].contains(s.substring(1, s.length()));
    }
  }

  public void add(String s) {
    if (s.isEmpty()) {
      this.isWord = true;
      return;
    } else if ( !Character.isLowerCase(s.charAt(0))) {
      throw new IllegalArgumentException("cannot accept non lower letter.");
    } else {
      int index = s.charAt(0) - 'a';
      if (this.children[index] == null) {
        this.children[index] = new Trie();
      }

      this.children[index].add(s.substring(1, s.length()));
    }
  }

  public static void main(String[] args) {
    Trie trie = new Trie();

    trie.add("ape");
    trie.add("apple");
    trie.add("cable");
    trie.add("car");
    trie.add("cart");
    trie.add("cat");
    trie.add("cattle");
    trie.add("curl");
    trie.add("far");
    trie.add("farm");

    System.out.println(trie.contains("ape"));
    System.out.println(trie.contains("apple"));
    System.out.println(trie.contains("farm"));
    System.out.println(trie.contains("xixixix"));
  }
}
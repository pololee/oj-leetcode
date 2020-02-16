package javasolutions.trie;

import java.util.HashMap;

public class TrieII {
  private boolean isWord;
  private String text;
  private HashMap<Character, TrieII> children;

  public TrieII() {
    isWord = false;
    text = "";
    children = new HashMap<Character, TrieII>();
  }

  public void add(String s) {
    if (s.isEmpty()) {
      isWord = true;
      return;
    } else if ( !Character.isLowerCase(s.charAt(0))) {
      throw new IllegalArgumentException("cannot accept non lower letter.");
    } else {
      char ch = s.charAt(0);

      if (!children.containsKey(ch)) {
        children.put(ch, new TrieII());
      }

      children.get(ch).add(s.substring(1, s.length()));
    }
  }

  public boolean contains(String s) {
    if (s.isEmpty()) {
      return isWord;
    } else if ( !Character.isLowerCase(s.charAt(0)) || !children.containsKey(s.charAt(0)) ) {
      return false;
    } else {
      return children.get(s.charAt(0)).contains(s.substring(1, s.length()));
    }
  }

  public static void main(String[] args) {
    TrieII trie = new TrieII();

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
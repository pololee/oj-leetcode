package javasolutions;

import java.util.Comparator;

public class BST <T extends Comparable<T>> {
	BSTNode<T> root;
	private Comparator<T> nodeComparator;

  public BST() {
    root = null;
    nodeComparator = null;
  }

  public BST(Comparator<T> comp) {
    root = null;
    nodeComparator = comp;
  }

  private int compare(T x, T y) {
    if (nodeComparator == null) {
      return x.compareTo(y);
    } else {
      return nodeComparator.compare(x, y);
    }
  }
}
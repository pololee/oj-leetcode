package javasolutions.learn;

import java.util.Comparator;

public class BinarySearchTree <T extends Comparable<T>> implements Iterable<T> {
  public static void main(String[] args) {
    
  }

  /**
   * the Node Class
   */
  private class Node<T> {
    private T data;
    private Node<T> left, right;

    public Node(T data, Node<T> leftNode, Node<T> rightNode) {
      left = leftNode;
      right = rightNode;
      this.data = data;
    }

    public Node(T data) {
      this(data, null, null);
    }

    public String toString() {
      return data.toString();
    }
  } // end of node

  /**
   * Basic setup of Binary Search Tree
   */
  private Node<T> root;
  private Comparator<T> nodeComparator;

  public BinarySearchTree() {
    root = null;
    nodeComparator = null;
  }

  public BinarySearchTree(Comparator<T> comp) {
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

  /**
   *  INSERT
   *  
   *  why do we use root = insert(root, data)?
   *  Because
   *   if the tree is empty, the passed root is null and we need to reset root
   *   to the node that was created by insert().
   *  In C and C++, we could use "reference parameters" to solve the problem.
   *  (Modify the original value.) However, in Java, we don't have such solutions
   *  So to make it simple, insert() will simply return the root(either new or old)
   *  and it's the caller's responsibility to use the returned (new or old) value.
   *
   *  Given a binary search tree and a number, inserts a new node with the given
   *  data in the correct place in the tree.
   *  Returns the new root pointer which the caller should then use (the standard
   *  trick to avoid using reference parameters)
   */
  public void insert(T data) {
    root = insert(root, data);
  }

  private Node<T> insert(Node<T> rootNode, T dataToInsert) {
    if (rootNode == null) {
      return new Node<T>(dataToInsert);
    }

    // do not allow to insert duplicate data
    if (compare(dataToInsert, rootNode.data) == 0) {
      return rootNode;
    }

    if (compare(dataToInsert, rootNode.data) < 0) {
      rootNode.left = insert(rootNode.left, dataToInsert);
    } else {
      rootNode.right = insert(rootNode.right, dataToInsert);
    }
    return rootNode;
  }

  /**
   *  SEARCH
   *
   *  Look up data to if it exists in the tree
   */
  
  public boolean lookup(T dataToLookUp) {
    return lookup(root, dataToLookUp);
  }

  private boolean lookup(Node<T> rootNode, T dataToLookUp) {
    if (rootNode == null) {
      return false;
    } else if (compare(dataToLookUp, rootNode.data) == 0) {
      return true;
    } else if (compare(dataToLookUp, rootNode.data) < 0) {
      return lookup(rootNode.left, dataToLookUp);
    } else {
      return lookup(rootNode.right, dataToLookUp);
    }
  }

  /**
   *  DELETE
   *
   *  Same idea as insert, we may change the root in delete(). So delete() will
   *  return the root(old or new) and the caller will reset the root
   *
   *  Delete is more tricky than search and insert. Situations to consider:
   *  1. dataToDelete is not in the tree
   *     there is nothing to delete, and simply return.
   *  2. dataToDelete is on the leaf node
   *     set its parent's pointer to the leaf(parant.left or parent.right) to null
   *  3. dataToDelete is on a node that has only one child.
   *     the procedure is identical to deleting a node from a linkded list.
   *  4. dataToDelete is on a node that has both left and right.
   *     Strategy: 
   *       find the largest node in the left subtree (node x) and replace the node
   *       being deleted with node x.
   *       OR find the smallest node in the right subtree (node y) and replace the node
   *       being deleted with node y
   *      
   */
  
  public void delete(T dataToDelete) {
    root = delete(root, dataToDelete);
  }

  private Node<T> delete(Node<T> rootNode, T dataToDelete) {
    if (rootNode == null) {
      throw new RuntimeException("cannot delete because cannot find the data");
    } else if (compare(dataToDelete, rootNode.data) < 0) {
      rootNode.left = delete(rootNode.left, dataToDelete);
    } else if (compare(dataToDelete, rootNode.data) > 0) {
      rootNode.right = delete(rootNode.right, dataToDelete);
    } else {
      if (rootNode.left == null) {
        return rootNode.right;
      } else if (rootNode.right == null) {
        return rootNode.right;
      } else {
        // find the largest node in the left subtree
        // i.e. get data from the rightmost node in the left subtree
        rootNode.data = retrieveRighmostNodeData(rootNode.left);
        // delete the rightmost node in the left subtree
        rootNode.left = delete(rootNode.left, rootNode.data);
      }
    }
    return rootNode;
  }

  private T retrieveRighmostNodeData(Node<T> rootNode) {
    while(rootNode.right != null) {
      rootNode = rootNode.right;
    }
    return rootNode.data;
  }

  /**
   *   TRAVERSAL
   */
  public void preOrderTraversal() {
    preOrderHelper(root);
  }

  private void preOrderHelper(Node<T> rootNode) {
    if (rootNode != null) {
      System.out.print(rootNode + " ");
      preOrderHelper(rootNode.left);
      preOrderHelper(rootNode.right);
    }
  }

  public void inOrderTraversal() {
    inOrderHelper(root);
  }

  private void inOrderHelper(Node<T> rootNode) {
    if (rootNode != null) {
      inOrderHelper(rootNode.left);
      System.out.print(rootNode + " ");
      inOrderHelper(rootNode.right);
    }
  }

  public void postOrderTraversal() {

  }

  private void postOrderHelper(Node<T> rootNode) {
    if (rootNode != null) {
      postOrderHelper(rootNode.left);
      postOrderHelper(rootNode.right);
      System.out.print(rootNode + " ");
    }
  }

  /**
   *   CLONE
   */
  
  public BinarySearchTree<T> clone() {
    BinarySearchTree<T> copy = nodeComparator == null ? new BinarySearchTree() : new BinarySearchTree(nodeComparator);
    copy.root = cloneHelper(root);
    return copy;
  }

  private Node<T> cloneHelper(Node<T> rootNode) {
    if (rootNode == null) {
      return null;
    } else {
      return new Node<T>(rootNode.data, cloneHelper(rootNode.left), cloneHelper(rootNode.right));
    }
  }
}
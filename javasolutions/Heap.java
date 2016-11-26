/**
 * A simple demo of binary heap
 */

package javasolutions;

import java.util.Arrays;

public class Heap<T extends Comparable<T>> {
  private static final int CAPACITY = 2;

  private int size;
  private T[] heap;

  public Heap() {
    size = 0;
    heap = (T[])new Comparable[CAPACITY];
  }

  public Heap(T[] array) {
    size = array.length;
    heap = (T[])new Comparable[array.length + 1];

    // The root is the second item in the array. 
    // We skip the index zero cell of the array for the convenience of implementation. 
    // Consider k-th element of the array, the
    //  - its left child is located at 2*k index 
    //  - its right child is located at 2*k+1. index 
    //  - its parent is located at k/2 index
    System.arraycopy(array, 0, heap, 1, array.length);
    buildHeap();
  }

  // Why we start with k = size/2?
  // Each leaf is a trivial subheap, because it doesn't have any child.
  // We may begin to percolatingDown(or Heapify) on each parent of a leaf.
  // Parents of leaves begin at index = size/2;
  private void buildHeap() {
    for (int k = size/2; k > 0; k--) {
      percolatingDown(k);
    }
  }

  private void percolatingDown(int k) {
    T tmp = heap[k];
    int currentPosition = k;
    int child;

    while(2*currentPosition <= size) {
      child = 2*currentPosition;

      // if node K has two children, pick the smallest child
      if (child != size && heap[child].compareTo(heap[child + 1]) > 0) {
        child++;
      }

      if (tmp.compareTo(heap[child]) > 0 ) {
        heap[currentPosition] = heap[child];
        currentPosition = child;
      } else {
        break;
      }
    }

    heap[currentPosition] = tmp;
  }

  public void heapSort(T[] array) {
    size = array.length;
    heap = (T[])new Comparable[size + 1];
    System.arraycopy(array, 0, heap, 1, size);
    buildHeap();

    for (int i = size; i > 0; i--) {
      T tmp = heap[i];
      heap[i] = heap[1];
      heap[1] = tmp; // swap root and the end of the heap array
      
      size--;
      percolatingDown(1);
    }

    for (int k = 0; k < heap.length - 1; k++) {
      array[k] = heap[heap.length - 1 - k];
    }
  }

  public T deleteMin() throws RuntimeException {
    if (size == 0) {
      throw new RuntimeException();
    }

    T min = heap[1];
    heap[1] = heap[size--];
    percolatingDown(1);
    return min;
  }

  public void insert(T x) {
    if (size == heap.length - 1) {
      doubleSize();
    }

    size = size + 1;
    int pos = size;
    while(pos > 1 && x.compareTo(heap[pos/2]) < 0) {
      heap[pos] = heap[pos/2];
      pos = pos/2;
    }

    heap[pos] = x;
  }

  private void doubleSize() {
    T[] old = heap;
    heap = (T[])new Comparable[heap.length * 2];
    System.arraycopy(old, 1, heap, 1, size);
  }

  public String toString() {
    String out = "";
    for (int k = 1; k <= size; k++) {
      out += heap[k] + " ";
    }
    return out;
  }

  public static void main(String[] args) {
    Heap<String> h = new Heap<String>();
    h.insert("p");
    h.insert("r");
    h.insert("i");
    h.insert("o");
    System.out.println(h);
    h.deleteMin();
    System.out.println(h);

    Heap<Integer> tmp = new Heap<Integer>();
    Integer[] a = {4,7,7,7,5,0,2,3,5,1};
    tmp.heapSort(a);
    System.out.println(Arrays.toString(a));
  }
}
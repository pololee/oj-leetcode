/**
https://leetcode.com/problems/lru-cache/description/
 It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. 
When the cache reached its capacity, 
it should invalidate the least recently used item before inserting a new item.
 */

package facebook.p146;

import java.util.HashMap;

public class LRUCache {
  static class Node {
    int key;
    int value;
    Node pre;
    Node next;

    public Node(int key, int value) {
      this.key = key;
      this.value = value;
      pre = null;
      next = null;
    }
  }

  int capacity;
  Node head;
  Node end;
  HashMap<Integer, Node> map;

  public LRUCache(int capacity) {
    this.capacity = capacity;
    head = null;
    end = null;
    map = new HashMap<>();
  }

  public int get(int key) {
    if (map.containsKey(key)) {
      Node node = map.get(key);
      remove(node);
      setHead(node);

      System.out.format("after get, the end key %d, value %d\n", end.key, end.value);
      return node.value;
    }

    return -1;
  }

  public void put(int key, int value) {
    System.out.format("key %d, value %d\n", key, value);
    if (map.containsKey(key)) {
      Node node = map.get(key);
      node.value = value;
      remove(node);
      setHead(node);
    } else {
      Node created = new Node(key, value);

      if (map.size() >= capacity) {
        System.out.format("remove end key %d, value %d\n", end.key, end.value);
        map.remove(end.key);
        remove(end);
      }

      map.put(key, created);
      setHead(created);
      System.out.format("map size %d\n", map.size());      
    }
  }

  private void remove(Node n) {
    if (n.pre != null) {
      n.pre.next = n.next;
    } else {
      head = n.next;
    }

    if (n.next != null) {
      n.next.pre = n.pre;
    } else {
      end = n.pre;
    }
  }

  private void setHead(Node n) {
    if (head == null) {
      head = n;
    } else {
      n.next = head;
      n.pre = null;
      head.pre = n;
      head = n;
    }

    if (end == null) {
      end = n;
    }
  }

  public void printHeadEnd() {
    System.out.format("head key %d\n", head.key);
    System.out.format("end key %d\n", end.key);
  }

  public static void main(String[] args) {
    LRUCache cache = new LRUCache(2);
    cache.put(1, 1);
    cache.put(2, 2);
    cache.printHeadEnd();
    System.out.println(cache.get(1));
    cache.put(3, 3);
    System.out.println(cache.get(2));
  }
}

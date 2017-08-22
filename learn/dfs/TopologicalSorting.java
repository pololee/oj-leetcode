package learn.dfs;

import java.util.Stack;
import java.util.LinkedList;

public class TopologicalSorting {
  static class Graph {
    private int numOfVertices;
    private LinkedList<Integer>[] adj; // ajacency list representation

    Graph(int num) {
      numOfVertices = num;
      adj = new LinkedList[numOfVertices];

      for(int i = 0; i < numOfVertices; i++) {
        adj[i] = new LinkedList<Integer>();
      }
    }

    void addEdge(int v, int w) {
      adj[v].add(w);
    }

    int getNumOfVertices() {
      return this.numOfVertices;
    }

    LinkedList<Integer>[] getAdjacencyList() {
      return this.adj;
    }
  }

  void topologicalSortUtil(int v, boolean[] visited, Stack<Integer> stack, Graph g) {
    visited[v] = true;

    LinkedList<Integer>[] adj = g.getAdjacencyList();
    for(Integer node : adj[v]) {
      if(!visited[node]) {
        topologicalSortUtil(node, visited, stack, g);
      }
    }

    stack.push(new Integer(v));
  }

  void topologicalSort(Graph g) {
    int num = g.getNumOfVertices();
    boolean[] visited = new boolean[num];
    Stack<Integer> stack = new Stack<>();

    for(int i = 0; i < num; i++) {
      if(!visited[i]) {
        topologicalSortUtil(i, visited, stack, g);
      }
    }

    while(!stack.isEmpty()) {
      System.out.format("%d ", stack.pop());
    }
  }

  public static void main(String[] args) {
    Graph g = new Graph(6);
    g.addEdge(5, 2);
    g.addEdge(5, 0);
    g.addEdge(4, 0);
    g.addEdge(4, 1);
    g.addEdge(2, 3);
    g.addEdge(3, 1);

    TopologicalSorting sort = new TopologicalSorting();

    System.out.println("Following is a Topological sorting of a given graph:");
    sort.topologicalSort(g);
  }
}
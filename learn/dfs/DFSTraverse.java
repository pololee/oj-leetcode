package learn.dfs;

import java.util.LinkedList;

public class DFSTraverse {
  private int numOfVertices;
  private LinkedList<Integer>[] adj; // Array of list for adjacency list representation

  DFSTraverse(int num) {
    numOfVertices = num;
    adj = new LinkedList[numOfVertices];

    for(int i = 0; i < numOfVertices; i++) {
      adj[i] = new LinkedList<Integer>();
    }
  }

  void addEdge(int v, int w) {
    adj[v].add(w);
  }

  void DFSUtil(int v, boolean[] visited) {
    visited[v] = true;
    System.out.format("%d ", v);

    for(Integer node : adj[v]) {
      if (!visited[node]) {
        DFSUtil(node, visited);
      }
    }
  }

  public void DFS() {
    boolean[] visited = new boolean[numOfVertices]; // default should be false

    for(int i = 0; i < numOfVertices; i++) {
      if(!visited[i]) {
        DFSUtil(i, visited);
      }
    }
  }

  public static void main(String[] args) {
    DFSTraverse graph = new DFSTraverse(4);

    graph.addEdge(0, 1);
    graph.addEdge(0, 2);
    graph.addEdge(1, 2);
    graph.addEdge(2, 0);
    graph.addEdge(2, 3);
    graph.addEdge(3, 3);
    
    System.out.println("Following is Depth first traversal:");
    graph.DFS();
  }
}
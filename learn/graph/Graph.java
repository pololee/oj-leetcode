/**
Use adjacency list to represent a graph
 */

package learn.graph;

import java.util.LinkedList;

public class Graph {
  private int numOfNodes;
  private LinkedList<Integer>[] adjacent;

  Graph(int numOfNodes) {
    this.numOfNodes = numOfNodes;
    adjacent = new LinkedList[numOfNodes];

    for(int i = 0; i < numOfNodes; i++) {
      adjacent[i] = new LinkedList<Integer>();
    }
  }

  void addEdge(int v, int w) {
    if(v >= numOfNodes || w >= numOfNodes) return;

    adjacent[v].add(w);
  }

  public LinkedList<Integer>[] getAdjacentList() {
    return this.adjacent;
  }

  public int getNumOfNodes() {
    return this.numOfNodes;
  }

  public static Graph dummyGraph() {
    Graph g = new Graph(4);

    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 3);

    return g;
  }
}
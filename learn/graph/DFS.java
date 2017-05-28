/**
http://www.geeksforgeeks.org/depth-first-traversal-for-a-graph/
 */

package learn.graph;

import learn.graph.Graph;
import java.util.LinkedList;

public class DFS {
  // this will cover all the nodes that are reachable from node s
  public void traverseDFS(int s, Graph g) {
    int numOfNodes = g.getNumOfNodes();
    if(s >= numOfNodes) return;

    boolean[] visited = new boolean[numOfNodes]; // default is false
    DFShelper(g, visited, s);
  }

  // this will cover all the nodes
  public void traverseDFSAll(Graph g) {
    int numOfNode = g.getNumOfNodes();
    boolean[] visited = new boolean[numOfNode];

    for(int i = 0; i < numOfNode; i++) {
      if(!visited[i]) {
        DFShelper(g, visited, i);
      }
    }
  }

  private void DFShelper(Graph g, boolean[] visited, int node) {
    visited[node] = true;
    System.out.print(node + " ");

    LinkedList<Integer>[] adjacent = g.getAdjacentList();
    for(Integer adjacentNode : adjacent[node]) {
      if(!visited[adjacentNode]) {
        DFShelper(g, visited, adjacentNode);
      }
    }
  }

  public static void main(String[] args) {
    Graph testG = Graph.dummyGraph();
    int start = 2;

    System.out.println("Following is Depth First Traversal " + "(starting from vertex 2)");

    DFS traverser = new DFS();
    traverser.traverseDFS(start, testG);
    System.out.println();

    System.out.println("DFS all nodes:");
    traverser.traverseDFSAll(testG);
  }
}
/**
http://www.geeksforgeeks.org/breadth-first-traversal-for-a-graph/
Java program to print BFS traversal from a given vertext
BFS(int s) traverses vertices reachable from vertex s
 */

package learn.graph;

import java.util.LinkedList;
import learn.graph.Graph;

public class BFS {
  //print BFS traversal from source s
  void traverseBFS(int s, Graph graph) {
    int numOfNodes = graph.getNumOfNodes();
    if(s >= numOfNodes) return;

    LinkedList<Integer>[] adjacent = graph.getAdjacentList();

    boolean[] visited = new boolean[numOfNodes]; //default is false
    visited[s] = true;

    LinkedList<Integer> queue = new LinkedList<>();
    queue.add(s);

    while(!queue.isEmpty()) {
      Integer node = queue.poll();
      System.out.print(node + " ");

      LinkedList<Integer> adjacentList = adjacent[node];
      for(Integer adjacentNode : adjacentList) {
        if(!visited[adjacentNode]) {
          queue.add(adjacentNode);
          visited[adjacentNode] = true;
        }
      }
    }
  }

  public static void main(String[] args) {
    Graph testGraph = Graph.dummyGraph();
    int startNode = 2;

    System.out.println("Following is Breadth First Traversal " + "(starting from vertex 2)");

    BFS traverser = new BFS();
    traverser.traverseBFS(startNode, testGraph);
  }
}
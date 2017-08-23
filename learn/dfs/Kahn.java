/**
Kahn's algorithmis for topological sorting
http://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/
 */

package learn.dfs;

import java.util.*;
import static learn.dfs.TopologicalSorting.Graph;

public class Kahn {
  void topologicalSorting(Graph g) {
    int numOfVertices = g.getNumOfVertices();
    LinkedList<Integer>[] adj = g.getAdjacencyList();

    // calculate indegree of each node, it take O(V+E)
    int[] indegrees = new int[numOfVertices];
    for(int i = 0; i < numOfVertices; i++) {
      for(Integer node : adj[i]) {
        indegrees[node]++;
      }
    }

    Queue<Integer> queue = new LinkedList<>();
    for(int i = 0; i < numOfVertices; i++) {
      if(indegrees[i] == 0) {
        queue.add(i);
      }
    }

    int numOfVisited = 0;
    List<Integer> sortedList = new LinkedList<>();
    while(!queue.isEmpty()) {
      int node = queue.remove();
      numOfVisited++;
      sortedList.add(new Integer(node));

      for(Integer neighbor : adj[node]) {
        indegrees[neighbor]--;
        
        if(indegrees[neighbor] == 0) {
          queue.add(neighbor);
        }
      }
    }

    if(numOfVisited != numOfVertices) {
      System.out.println("The graph has one or more loops");
      return;
    }

    for(Integer node : sortedList) {
      System.out.format("%d ", node);
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

    Kahn sort = new Kahn();
    sort.topologicalSorting(g);
  }
}

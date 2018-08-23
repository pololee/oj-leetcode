/**
in fast dijkstra, we use PriorityQueue to speed up the algorithm
 */
package learn.fastDijkstra.model;

import java.util.Map;
import java.util.HashMap;
import java.util.Set;

public class Node {
  private final String id;
  private Map<Node, Integer> adjacentNodes;

  public Node(String id) {
    this.id = id;
    adjacentNodes = new HashMap<>();
  }

  public void addEdge(Node destination, int weight) {
    adjacentNodes.put(destination, weight);
  }

  public Set<Node> getAdjacentNodesSet() {
    return this.adjacentNodes.keySet();
  }

  public String getId() {
    return this.id;
  }

  public int getEdgeWeight(Node destination) {
    if(adjacentNodes.containsKey(destination)) {
      return adjacentNodes.get(destination);
    } else {
      return Integer.MAX_VALUE;
    }
  }
}

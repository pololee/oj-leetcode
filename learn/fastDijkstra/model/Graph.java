/**
in fast dijkstra, we use PriorityQueue to speed up the algorithm
 */

package learn.fastDijkstra.model;

import java.util.List;
import java.util.ArrayList;

public class Graph {
  private final int numOfNodes;
  private final List<Node> nodes;

  public Graph(int numOfNodes) {
    this.numOfNodes = numOfNodes;
    nodes = new ArrayList<>();
  }

  public int getNumOfNodes() {
    return this.numOfNodes;
  }

  public List<Node> getNodes() {
    return this.nodes;
  }

  public void addNode(Node node) {
    nodes.add(node);
  }
}


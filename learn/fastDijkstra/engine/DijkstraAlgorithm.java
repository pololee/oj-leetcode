/**
 *
 * in fast dijkstra, we use PriorityQueue to speed up the algorithm
 */

package learn.fastDijkstra.engine;

import learn.fastDijkstra.model.Node;
import learn.fastDijkstra.model.Graph;
import learn.fastDijkstra.model.DijkstraNode;

import java.util.PriorityQueue;
import java.util.List;
import java.util.LinkedList;
import java.util.Map;
import java.util.HashMap;

public class DijkstraAlgorithm {
  private PriorityQueue<DijkstraNode> distanceQueue;
  private final Map<Node, DijkstraNode> nodeMap;

  public DijkstraAlgorithm(Graph graph) {
    nodeMap = new HashMap<>();

    for(Node node : graph.getNodes()) {
      DijkstraNode dijkNode = new DijkstraNode(node);
      nodeMap.put(node, dijkNode);
    }
  }

  public void execute(Node source) {
    DijkstraNode sourceDijk = nodeMap.get(source);
    sourceDijk.setDistance(0);
    distanceQueue = new PriorityQueue<>();
    distanceQueue.add(sourceDijk);

    while(!distanceQueue.isEmpty()) {
      DijkstraNode dijkNode = distanceQueue.poll();
      dijkNode.setSettled();
      relax(dijkNode);
    }
  }

  /**
   * relax function is to update the distance 
   * with this dijkNode, we can now reach more nodes.
   * So we need to update the distance for thoese nodes
   */

  private void relax(DijkstraNode dijkNode) {
    Node originalNode = dijkNode.getOriginalNode();

    for(Node neighborNode : getNeighbors(originalNode)) {
      DijkstraNode neighborDijkNode = nodeMap.get(neighborNode);
      int oldDistance = neighborDijkNode.getDistance();
      int newDistance = dijkNode.getDistance() + originalNode.getEdgeWeight(neighborNode);

      if(oldDistance > newDistance) {
        neighborDijkNode.setDistance(newDistance);
        neighborDijkNode.setPredecessor(dijkNode);
        // https://stackoverflow.com/questions/1871253/updating-java-priorityqueue-when-its-elements-change-priority
        // you have to remove and re-insert the node, because ProrityQueue won't update automatically.
        // it works by putting the new element at the right position
        distanceQueue.remove(neighborDijkNode);
        distanceQueue.add(neighborDijkNode);
      }
    }
  }

  /**
   * getNeighbors return the neighbors of the input node.
   * Note: we only consider unsettled nodes here
   * @param  node [description]
   * @return      [description]
   */
  private List<Node> getNeighbors(Node node) {
    List<Node> neighbors = new LinkedList<>();

    for(Node adjacent : node.getAdjacentNodesSet()) {
      if(!isSettled(adjacent)) {
        neighbors.add(adjacent);
      }
    }

    return neighbors;
  }

  private boolean isSettled(Node node) {
    return nodeMap.get(node).isSettled();
  }

  public void printDistance() {
    System.out.println("Print all node's distance:");
    for(Map.Entry<Node, DijkstraNode> entry : nodeMap.entrySet()) {
      Node originalNode = entry.getKey();
      DijkstraNode dijkNode = entry.getValue();

      System.out.format("Node ID: %s, distance: %d, predecessor node id: %s\n", 
        originalNode.getId(), 
        dijkNode.getDistance(), 
        dijkNode.getPredecessorNodeId());
    }
  }
}

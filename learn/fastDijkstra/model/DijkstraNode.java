/**
 *
 * in fast dijkstra, we use PriorityQueue to speed up the algorithm
 */

package learn.fastDijkstra.model;


public class DijkstraNode implements Comparable<DijkstraNode> {
  private final Node originalNode;
  private int distance;
  private DijkstraNode predecessor;
  private boolean settled;

  public DijkstraNode(Node originalNode) {
    this.originalNode = originalNode;
    distance = Integer.MAX_VALUE;
    predecessor = null;
    settled = false;
  }

  public Node getOriginalNode() {
    return this.originalNode;
  }

  public void setDistance(int distance) {
    this.distance = distance;
  }

  public int getDistance() {
    return this.distance;
  }

  public void setPredecessor(DijkstraNode predecessor) {
    this.predecessor = predecessor;
  }

  public String getPredecessorNodeId() {
    if(predecessor == null) {
      return "null";
    } else {
      return predecessor.originalNode.getId();
    }
  }

  public boolean isSettled() {
    return this.settled;
  }

  public void setSettled() {
    this.settled = true;
  }

  @Override
  public int compareTo(DijkstraNode other) {
    if(this.getDistance() < other.getDistance()) {
      return -1;
    } else if(this.getDistance() > other.getDistance()) {
      return 1;
    } else {
      return 0;
    }
  }
}

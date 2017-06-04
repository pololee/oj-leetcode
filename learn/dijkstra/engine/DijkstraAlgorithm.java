package learn.dijkstra.engine;

import learn.dijkstra.model.Vertex;
import learn.dijkstra.model.Edge;
import learn.dijkstra.model.Graph;

import java.util.List;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Set;
import java.util.HashSet;
import java.util.Map;
import java.util.HashMap;

public class DijkstraAlgorithm {
  private final List<Vertex> vertexes;
  private final List<Edge> edges;
  private Set<Vertex> settledNodes;
  private Set<Vertex> unSettledNodes;
  private Map<Vertex, Vertex> predecessors;
  private Map<Vertex, Integer> currentDistance;

  public DijkstraAlgorithm(Graph graph) {
    this.vertexes = new ArrayList<Vertex>(graph.getVertexes());
    this.edges = new ArrayList<Edge>(graph.getEdges());
  }

  public void execute(Vertex source) {
    settledNodes = new HashSet<Vertex>();
    unSettledNodes = new HashSet<Vertex>();
    predecessors = new HashMap<Vertex, Vertex>();
    currentDistance = new HashMap<Vertex, Integer>();
    currentDistance.put(source, 0);
    unSettledNodes.add(source);

    while(!unSettledNodes.isEmpty()) {
      Vertex node = getMinimumDistance(unSettledNodes);
      settledNodes.add(node);
      unSettledNodes.remove(node);
      updateCurrentDistance(node);
    }
  }

  /**
  Among the unsettled nodes, find the node which has the minimum distance
  from source to itself.
   */
  private Vertex getMinimumDistance(Set<Vertex> vertexes) {
    Vertex minimum = null;
    for(Vertex vertex : vertexes) {
      if(minimum == null || getCurrentDistance(vertex) < getCurrentDistance(minimum)) {
        minimum = vertex;
      }
    }

    return minimum;
  }

  /**
  The currentDistance store all the distances from source to each node at
  current step. Not every node is reachable for now. The distance of a node,
  which is not reachable for now, is unlimited. We use Integer.MAX_VALUE to
  represent it.
   */
  private int getCurrentDistance(Vertex destination) {
    Integer dist = currentDistance.get(destination);

    return dist == null ? Integer.MAX_VALUE : dist;
  }

  /**
  Once we add a new node into settled nodes, we are able to reach more nodes, which
  are the adjacent nodes of the new node we just added.
  Those nodes could be already in the reachable nodes (i.e. unSettledNodes), which
  have distances. But once we add the new node, the distance might get changed.
  So we need to update the current distance.
   */
  private void updateCurrentDistance(Vertex node) {
    List<Vertex> adjacentNodes = getNeighbors(node);

    for(Vertex adjacent : adjacentNodes) {
      int oldDistance = getCurrentDistance(adjacent);
      int newDistance = getCurrentDistance(node) + getEdgeWeight(node, adjacent);

      if(oldDistance > newDistance) {
        currentDistance.put(adjacent, new Integer(newDistance));
        predecessors.put(adjacent, node);
        unSettledNodes.add(adjacent);
      }
    }
  }

  private List<Vertex> getNeighbors(Vertex node) {
    List<Vertex> neighbors = new ArrayList<Vertex>();
    for(Edge edge : edges) {
      Vertex source = edge.getSource();
      Vertex destination = edge.getDestination();

      if(source.equals(node) && !isSettled(destination)) {
        neighbors.add(destination);
      }
    }

    return neighbors;
  }

  private boolean isSettled(Vertex node) {
    return settledNodes.contains(node);
  }

  private int getEdgeWeight(Vertex source, Vertex destination) {
    for(Edge edge : edges) {
      if(source.equals(edge.getSource()) && destination.equals(edge.getDestination())) {
        return edge.getWeight();
      }
    }

    throw new RuntimeException("Should not happen");
  }
}

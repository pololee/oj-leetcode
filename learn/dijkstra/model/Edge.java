package learn.dijkstra.model;

public class Edge {
  private final Vertex source;
  private final Vertex destination;
  private final String id;
  private final int weight;

  public Edge(Vertex source, Vertex destination, String id, int weight) {
    this.source = source;
    this.destination = destination;
    this.id = id;
    this.weight = weight;
  }

  public Vertex getSource() {
    return source;
  }

  public Vertex getDestination() {
    return destination;
  }

  public String getId() {
    return id;
  }

  public int getWeight() {
    return weight;
  }

  @Override
  public String toString() {
    return source + "->" + destination;
  }
}
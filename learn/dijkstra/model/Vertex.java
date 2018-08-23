package learn.dijkstra.model;

public class Vertex {
  private final String id;
  private final String name;

  public Vertex(String id, String name) {
    this.id = id;
    this.name = name;
  }

  public String getId() {
    return id;
  }

  public String getName() {
    return name;
  }

  @Override
  public boolean equals(Object obj) {
    if(this == obj) {
      return true;
    }

    if(obj == null) {
      return false;
    }

    if(getClass() != obj.getClass()) {
      return false;
    }

    Vertex other = (Vertex) obj;
    if(this.id != other.id) {
      return false;
    }

    return true;
  }

  @Override
  public String toString() {
    return name;
  }
}
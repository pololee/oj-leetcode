/**
 *
 * in fast dijkstra, we use PriorityQueue to speed up the algorithm
 */

package learn.fastDijkstra;

import learn.fastDijkstra.model.Node;
import learn.fastDijkstra.model.Graph;

import learn.fastDijkstra.engine.DijkstraAlgorithm;

public class TestAlgorithm {
  public static void main(String[] args) {
    // the graph is from http://www.baeldung.com/java-dijkstra
    Graph graph = new Graph(6);

    Node a = new Node("A");
    Node b = new Node("B");
    Node c = new Node("C");
    Node d = new Node("D");
    Node e = new Node("E");
    Node f = new Node("F");

    graph.addNode(a);
    graph.addNode(b);
    graph.addNode(c);
    graph.addNode(d);
    graph.addNode(e);
    graph.addNode(f);

    a.addEdge(b, 10);
    a.addEdge(c, 15);
    b.addEdge(f, 15);
    b.addEdge(d, 12);
    c.addEdge(e, 10);
    d.addEdge(f, 1);
    d.addEdge(e, 2);
    f.addEdge(e, 5);

    DijkstraAlgorithm dijkstra = new DijkstraAlgorithm(graph);
    dijkstra.execute(a);
    dijkstra.printDistance();
  }
}

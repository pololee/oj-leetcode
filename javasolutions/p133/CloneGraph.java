package javasolutions.p133;

import javasolutions.p133.UndirectedGraphNode;
import java.util.Map;
import java.util.HashMap;

import java.util.Queue;
import java.util.LinkedList;

public class CloneGraph {
  public UndirectedGraphNode clone(UndirectedGraphNode graph) {
    if(graph == null) return null;

    Map<UndirectedGraphNode, UndirectedGraphNode> map = new HashMap<>();
    return DFS(graph, map);
  }

  private UndirectedGraphNode DFS(UndirectedGraphNode graph, Map<UndirectedGraphNode, UndirectedGraphNode> map) {
    if(map.containsKey(graph)) return map.get(graph);

    UndirectedGraphNode copied = new UndirectedGraphNode(graph.label);
    map.put(graph, copied);

    for(UndirectedGraphNode neighbor : graph.neighbors) {
      copied.neighbors.add(DFS(neighbor, map));
    }

    return copied;
  }

  public UndirectedGraphNode cloneBFS(UndirectedGraphNode graph) {
    if(graph == null) return null;

    Queue<UndirectedGraphNode> queue = new LinkedList<>();
    queue.add(graph);
    UndirectedGraphNode copied = new UndirectedGraphNode(graph.label);
    Map<UndirectedGraphNode, UndirectedGraphNode> map = new HashMap<>();
    map.put(graph, copied);

    while(!queue.isEmpty()) {
      UndirectedGraphNode originalNode = queue.poll();

      for(UndirectedGraphNode originalNeighbor : originalNode.neighbors) {
        if (map.containsKey(originalNeighbor)) {
          UndirectedGraphNode copiedNode = map.get(originalNode);
          copiedNode.neighbors.add(map.get(originalNeighbor));
        } else {
          UndirectedGraphNode copiedNeighbor = new UndirectedGraphNode(originalNeighbor.label);
          UndirectedGraphNode copiedNode = map.get(originalNode);
          copiedNode.neighbors.add(copiedNeighbor);

          map.put(originalNeighbor, copiedNeighbor);
          queue.offer(originalNeighbor);
        }
      }
    }

    return copied;
  }
}
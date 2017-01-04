package javasolutions.leetcodeBook;

import javasolutions.leetcodeBook.UndirectedGraphNode;

import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;

public class CloneGraph {
  public UndirectedGraphNode clone(UndirectedGraphNode node) {
    if(node == null) return null;
    Map<UndirectedGraphNode, UndirectedGraphNode> map = new HashMap<>();
    return DFSCopy(map, node);
  }

  private UndirectedGraphNode DFSCopy(Map<UndirectedGraphNode, UndirectedGraphNode> map, UndirectedGraphNode originalNode) {
    if(map.containsKey(originalNode)) {
      return map.get(originalNode);
    }

    UndirectedGraphNode copied = new UndirectedGraphNode(originalNode.label);
    map.put(originalNode, copied);
    
    for(UndirectedGraphNode node : originalNode.neighbors) {
      copied.neighbors.add(DFSCopy(map, node));
    }

    return copied;
  }
}
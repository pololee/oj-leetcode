Dijkstra's algorithm uses a priority queue to greedily select the closest vertex that has not yet been processed, and performs this relaxation process on all of its outgoing edges; by contrast, the Bellman–Ford algorithm simply relaxes all the edges, and does this {\displaystyle |V|-1} |V|-1 times, where {\displaystyle |V|} |V| is the number of vertices in the graph.

```
function BellmanFord(list vertices, list edges, vertex source)
   ::distance[],predecessor[]

   // This implementation takes in a graph, represented as
   // lists of vertices and edges, and fills two arrays
   // (distance and predecessor) with shortest-path
   // (less cost/distance/metric) information

   // Step 1: initialize graph
   for each vertex v in vertices:
       distance[v] := inf             // At the beginning , all vertices have a weight of infinity
       predecessor[v] := null         // And a null predecessor

   distance[source] := 0              // The weight is zero at the source

   // Step 2: relax edges repeatedly
   for i from 1 to size(vertices)-1:
       for each edge (u, v) with weight w in edges:
           if distance[u] + w < distance[v]:
               distance[v] := distance[u] + w
               predecessor[v] := u

   // Step 3: check for negative-weight cycles
   for each edge (u, v) with weight w in edges:
       if distance[u] + w < distance[v]:
           error "Graph contains a negative-weight cycle"

   return distance[], predecessor[]
```

Simply put, the algorithm initializes the distance to the source to 0 and all other nodes to infinity. Then for all edges, if the distance to the destination can be shortened by taking the edge, the distance is updated to the new lower value. At each iteration {\displaystyle i} i that the edges are scanned, the algorithm finds all shortest paths of at most length {\displaystyle i} i edges (and possibly some paths longer than {\displaystyle i} i edges). Since the longest possible path without a cycle can be {\displaystyle |V|-1} |V|-1 edges, the edges must be scanned {\displaystyle |V|-1} |V|-1 times to ensure the shortest path has been found for all nodes. A final scan of all the edges is performed and if any distance is updated, then a path of length {\displaystyle |V|} |V| edges has been found which can only occur if at least one negative cycle exists in the graph.

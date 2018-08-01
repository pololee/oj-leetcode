 ## Pseudo Code
 ```
 1  function Dijkstra(Graph, source):
 2
 3      create vertex set Q
 4
 5      for each vertex v in Graph:             // Initialization
 6          dist[v] ← INFINITY                  // Unknown distance from source to v
 7          prev[v] ← UNDEFINED                 // Previous node in optimal path from source
 8          add v to Q                          // All nodes initially in Q (unvisited nodes)
 9
10      dist[source] ← 0                        // Distance from source to source
11      
12      while Q is not empty:
13          u ← vertex in Q with min dist[u]    // Node with the least distance
14                                              // will be selected first
15          remove u from Q 
16          
17          for each neighbor v of u:           // where v is still in Q.
18              alt ← dist[u] + length(u, v)
19              if alt < dist[v]:               // A shorter path to v has been found
20                  dist[v] ← alt 
21                  prev[v] ← u 
22
23      return dist[], prev[]
```

## Print the path
```
1  S ← empty sequence
2  u ← target
3  while prev[u] is defined:                 // Construct the shortest path with a stack S
4      insert u at the beginning of S        // Push the vertex onto the stack
5      u ← prev[u]                           // Traverse from target to source
6  insert u at the beginning of S            // Push the source onto the stack
```

## Using a Priority Queue
```
1  function Dijkstra(Graph, source):
2      dist[source] ← 0                           // Initialization
3
4      create vertex set Q
5
6      for each vertex v in Graph:           
7          if v ≠ source
8              dist[v] ← INFINITY                 // Unknown distance from source to v
9          prev[v] ← UNDEFINED                    // Predecessor of v
10
11         Q.add_with_priority(v, dist[v])
12
13
14     while Q is not empty:                      // The main loop
15         u ← Q.extract_min()                    // Remove and return best vertex
16         for each neighbor v of u:              // only v that are still in Q
17             alt ← dist[u] + length(u, v) 
18             if alt < dist[v]
19                 dist[v] ← alt
20                 prev[v] ← u
21                 Q.decrease_priority(v, alt)
22
23     return dist, prev
```
Instead of filling the priority queue with all nodes in the initialization phase, it is also possible to initialize it to contain only source; then, inside the if alt < dist[v] block, the node must be inserted if not already in the queue (instead of performing a decrease_priority operation



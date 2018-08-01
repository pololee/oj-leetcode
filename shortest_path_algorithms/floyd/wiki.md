Consider a graph {\displaystyle G} G with vertices {\displaystyle V} V numbered 1 through  {\displaystyle N} N. Further consider a function {\displaystyle \mathrm {shortestPath} (i,j,k)} {\displaystyle \mathrm {shortestPath} (i,j,k)} that returns the shortest possible path from {\displaystyle i} i to {\displaystyle j} j using vertices only from the set {\displaystyle \{1,2,\ldots ,k\}} {\displaystyle \{1,2,\ldots ,k\}} as intermediate points along the way. Now, given this function, our goal is to find the shortest path from each {\displaystyle i} i to each {\displaystyle j} j using only vertices in {\displaystyle \{1,2,\ldots ,N\}} \{1,2,\ldots ,N\}.

For each of these pairs of vertices, the {\displaystyle \mathrm {shortestPath} (i,j,k)} {\displaystyle \mathrm {shortestPath} (i,j,k)} could be either

(1) a path that doesn't go through {\displaystyle k} k (only uses vertices in the set {\displaystyle \{1,\ldots ,k-1\}} {\displaystyle \{1,\ldots ,k-1\}}.)
or

(2) a path that does go through {\displaystyle k} k (from {\displaystyle i} i to {\displaystyle k} k and then from {\displaystyle k} k to {\displaystyle j} j, both only using intermediate vertices in  {\displaystyle \{1,\ldots ,k-1\}} {\displaystyle \{1,\ldots ,k-1\}})
We know that the best path from {\displaystyle i} i to {\displaystyle j} j that only uses vertices {\displaystyle 1} 1 through {\displaystyle k-1} k-1 is defined by {\displaystyle \mathrm {shortestPath} (i,j,k-1)} {\displaystyle \mathrm {shortestPath} (i,j,k-1)}, and it is clear that if there were a better path from {\displaystyle i} i to {\displaystyle k} k to {\displaystyle j} j, then the length of this path would be the concatenation of the shortest path from {\displaystyle i} i to {\displaystyle k} k (only using intermediate vertices in {\displaystyle \{1,\ldots ,k-1\}} {\displaystyle \{1,\ldots ,k-1\}}) and the shortest path from {\displaystyle k} k to {\displaystyle j} j (only using intermediate vertices in  {\displaystyle \{1,\ldots ,k-1\}} {\displaystyle \{1,\ldots ,k-1\}}).

If {\displaystyle w(i,j)} {\displaystyle w(i,j)} is the weight of the edge between vertices {\displaystyle i} i and {\displaystyle j} j, we can define {\displaystyle \mathrm {shortestPath} (i,j,k)} {\displaystyle \mathrm {shortestPath} (i,j,k)} in terms of the following recursive formula: the base case is

{\displaystyle \mathrm {shortestPath} (i,j,0)=w(i,j)} {\displaystyle \mathrm {shortestPath} (i,j,0)=w(i,j)}
and the recursive case is

{\displaystyle \mathrm {shortestPath} (i,j,k)=} {\displaystyle \mathrm {shortestPath} (i,j,k)=}
{\displaystyle \mathrm {min} {\Big (}\mathrm {shortestPath} (i,j,k-1),} {\displaystyle \mathrm {min} {\Big (}\mathrm {shortestPath} (i,j,k-1),}
{\displaystyle \mathrm {shortestPath} (i,k,k-1)+\mathrm {shortestPath} (k,j,k-1){\Big )}} {\displaystyle \mathrm {shortestPath} (i,k,k-1)+\mathrm {shortestPath} (k,j,k-1){\Big )}}.
This formula is the heart of the Floyd–Warshall algorithm. The algorithm works by first computing {\displaystyle \mathrm {shortestPath} (i,j,k)} {\displaystyle \mathrm {shortestPath} (i,j,k)} for all {\displaystyle (i,j)} (i,j) pairs for {\displaystyle k=1} k=1, then {\displaystyle k=2} k=2, etc. This process continues until {\displaystyle k=N} k=N, and we have found the shortest path for all {\displaystyle (i,j)} (i,j) pairs using any intermediate vertices. Pseudocode for this basic version follows:

```
1 let dist be a |V| × |V| array of minimum distances initialized to ∞ (infinity)
2 for each edge (u,v)
3    dist[u][v] ← w(u,v)  // the weight of the edge (u,v)
4 for each vertex v
5    dist[v][v] ← 0
6 for k from 1 to |V|
7    for i from 1 to |V|
8       for j from 1 to |V|
9          if dist[i][j] > dist[i][k] + dist[k][j] 
10             dist[i][j] ← dist[i][k] + dist[k][j]
11         end if

```

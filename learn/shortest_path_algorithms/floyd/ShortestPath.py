import sys


class ShortestPath:
    def floyd(self, V, edges):
        dist = [[sys.maxsize for _ in range(V)] for _ in range(V)]

        for u in range(V):
            for w in range(V):
                if edges[u][w]:
                    dist[u][w] = edges[u][w]
        for u in range(V):
            dist[u][u] = 0
        
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    if dist[i][k] != sys.maxsize and dist[k][j] != sys.maxsize and dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        print(dist)


def main():
    V = 4
    edges = [[None for _ in range(4)] for _ in range(4)]
    edges[0][2] = -2
    edges[1][0] = 4
    edges[1][2] = 3
    edges[2][3] = 2
    edges[3][1] = -1

    shortest = ShortestPath()
    shortest.floyd(V, edges)


if __name__ == '__main__':
    main()

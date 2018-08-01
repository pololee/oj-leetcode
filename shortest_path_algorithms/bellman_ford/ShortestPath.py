import sys


class ShortestPath:
    def bellman_ford(self, V, edges, src):
        """
        :V int: number of nodes
        :edges list[(src, dst, weight)]
        :srt int: src node index
        """

        # Step 1: initialize distance with infinite value,
        # distance[src] = 0
        distance = [sys.maxsize for _ in range(V)]
        distance[src] = 0

        # Step 2: Relax all edges |V| - 1 times. A simple
        # shortest path from src to any other vertex can
        # have at-most |V| - 1 edges
        for _ in range(V-1):
            for e_src, e_dst, e_weight in edges:
                if distance[e_src] != sys.maxsize and distance[e_src] + e_weight < distance[e_dst]:
                    distance[e_dst] = distance[e_src] + e_weight

        # Step 3: check for negative-weight cycles.  The above
        # step guarantees shortest distances if graph doesn't
        # contain negative weight cycle. If we get a shorter
        # path, then there is a cycle.
        for e_src, e_dst, e_weight in edges:
            if distance[e_src] != sys.maxsize and distance[e_src] + e_weight < distance[e_dst]:
                print("Graph contains negative weight cycle")

        print("Vertex   Distance from Source")
        for idx, value in enumerate(distance):
            print("{:^10}{:^10}".format(idx, value))


def main():
    V = 5
    edges = []
    edges.append((0, 1, -1))
    edges.append((0, 2, 4))
    edges.append((1, 2, 3))
    edges.append((1, 3, 2))
    edges.append((1, 4, 2))
    edges.append((3, 1, 1))
    edges.append((3, 2, 5))
    edges.append((4, 3, -3))

    bellman_ford = ShortestPath()
    bellman_ford.bellman_ford(V, edges, 0)
if __name__ == '__main__':
    main()

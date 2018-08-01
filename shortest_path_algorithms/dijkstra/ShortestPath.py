import heapq
import collections
import sys


class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        return heapq.heappop(self.heap)

    def is_empty(self):
        return len(self.heap) == 0


class ShortestPath:
    def dijkstra(self, graph, src):
        """
        :graph list[list[int]] graph[u][w] represent the cost from u to w
        :srt int: the start position
        """
        # initialize adjacency table representation of graph
        adj_table = collections.defaultdict(list)
        for u in range(len(graph)):
            for w in range(len(graph[u])):
                # tuple, item[0] cost, item[1] dest idx
                if graph[u][w] > 0:
                    item = (graph[u][w], w)
                    adj_table[u].append(item)

        V = len(adj_table.keys())

        distance = [sys.maxsize for _ in range(V)]
        prev = [None for _ in range(V)]
        distance[src] = 0
        min_heap = MinHeap()
        min_heap.push((0, src))

        while not min_heap.is_empty():
            _, vertex = min_heap.pop()

            for cost, neighbor in adj_table[vertex]:
                alt_distance = distance[vertex] + cost
                if alt_distance < distance[neighbor]:
                    distance[neighbor] = alt_distance
                    prev[neighbor] = vertex
                    min_heap.push((distance[neighbor], neighbor))
        return distance, prev


def main():
    graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
             [4, 0, 8, 0, 0, 0, 0, 11, 0],
             [0, 8, 0, 7, 0, 4, 0, 0, 2],
             [0, 0, 7, 0, 9, 14, 0, 0, 0],
             [0, 0, 0, 9, 0, 10, 0, 0, 0],
             [0, 0, 4, 14, 10, 0, 2, 0, 0],
             [0, 0, 0, 0, 0, 2, 0, 1, 6],
             [8, 11, 0, 0, 0, 0, 1, 0, 7],
             [0, 0, 2, 0, 0, 0, 6, 7, 0]]
    shortest_path = ShortestPath()
    distance, prev = shortest_path.dijkstra(graph, 0)
    print("Vertex   Distance from Source")
    for idx, value in enumerate(distance):
        print("{:^10}{:^10}".format(idx, value))


if __name__ == '__main__':
    main()

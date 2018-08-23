import sys
import collections
import heapq


class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, cost, vertex, stops_allowed):
        heapq.heappush(self.heap, (cost, vertex, stops_allowed))

    def pop(self):
        return heapq.heappop(self.heap)

    def empty(self):
        return len(self.heap) == 0


class MinHeapSolution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        if not flights:
            return -1

        adj_table = collections.defaultdict(list)
        for f_src, f_dst, f_price in flights:
            adj_table[f_src].append((f_dst, f_price))

        min_heap = MinHeap()
        min_heap.push(0, src, K + 1)

        while not min_heap.empty():
            print(min_heap.heap)
            m_cost, m_vertex, m_stops_allowed = min_heap.pop()

            if m_vertex == dst:
                return m_cost

            if m_stops_allowed > 0:
                for adj_neighbor, adj_price in adj_table[m_vertex]:
                    min_heap.push(
                        m_cost + adj_price,
                        adj_neighbor,
                        m_stops_allowed - 1
                    )

        return -1


def main():
    sol = MinHeapSolution()
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1
    # print(sol.findCheapestPrice(n, flights, src, dst, k))  # 200

    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 0
    # print(sol.findCheapestPrice(n, flights, src, dst, k))  # 500

    n = 5
    flights = [[4, 1, 1], [1, 2, 3], [0, 3, 2],
               [0, 4, 10], [3, 1, 1], [1, 4, 3]]
    src = 2
    dst = 1
    k = 1
    # print(sol.findCheapestPrice(n, flights, src, dst, k))  # -1

    n = 4
    flights = [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]]
    src = 0
    dst = 3
    k = 1
    print(sol.findCheapestPrice(n, flights, src, dst, k))  # 6


if __name__ == '__main__':
    main()

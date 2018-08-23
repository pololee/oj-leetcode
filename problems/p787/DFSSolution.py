import sys
import collections


class DFSSolution:
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

        self.answer = sys.maxsize

        adj_table = collections.defaultdict(list)
        for f_src, f_dst, f_price in flights:
            adj_table[f_src].append((f_dst, f_price))
        visited = [False for _ in range(n)]
        visited[src] = True
        self.dfs_util(src, dst, K + 1, 0, visited, adj_table)

        if self.answer != sys.maxsize:
            return self.answer

        return -1

    def dfs_util(self, cur, dst, stops, cost_sofar, visited, adj_table):
        if cur == dst:
            self.answer = cost_sofar
            return

        if stops <= 0:
            return

        for neighbor, price in adj_table[cur]:
            # Do not visit the same city twice
            if visited[neighbor]:
                continue
            # IMPORTANT! Pruning.
            # Why? self.answer represent the minimum price we found so far
            # so if the cost_sofar + price is larger than the self.answer
            # we found, there is no point of keeping going down this route
            # because the cost will only get bigger.
            if cost_sofar + price > self.answer:
                continue

            visited[neighbor] = True
            self.dfs_util(
                neighbor,
                dst,
                stops - 1,
                cost_sofar + price,
                visited,
                adj_table
            )
            visited[neighbor] = False


def main():
    sol = DFSSolution()
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1
    print(sol.findCheapestPrice(n, flights, src, dst, k)) # 200

    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 0
    print(sol.findCheapestPrice(n, flights, src, dst, k)) # 500

    n = 5
    flights = [[4, 1, 1], [1, 2, 3], [0, 3, 2],
               [0, 4, 10], [3, 1, 1], [1, 4, 3]]
    src = 2
    dst = 1
    k = 1
    print(sol.findCheapestPrice(n, flights, src, dst, k)) # -1


if __name__ == '__main__':
    main()

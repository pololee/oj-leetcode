from collections import deque
import sys

class Solution:
    """
    @param n: a integer
    @param flights: a 2D array
    @param src: a integer
    @param dst: a integer
    @param K: a integer
    @return: return a integer
    """

    def findCheapestPrice(self, n, flights, src, dst, K):
        # write your code here
        table = self.buildGraph(n, flights)

        level = 0
        ans = sys.maxsize
        queue = deque()
        queue.append((src, 0))

        print(table)

        while queue:
            if level > K + 1:
                break

            size = len(queue)
            for _ in range(size):
                node, cost = queue.popleft()
                print(node)

                if node == dst:
                    ans = min(ans, cost)
                for neigh, price in table[node]:
                    if cost + price > ans:
                        continue
                    queue.append((neigh, cost + price))

            level += 1

        if ans == sys.maxsize:
            return -1
        return ans

    def buildGraph(self, n, flights):
        table = dict()
        # this is the stupid part.
        # Different from BFSSolution, which uses collections.defaultdict()
        # when access a non-exist key, it will just give the default value list()
        for i in range(n):
            table[i] = list()

        for u, v, cost in flights:
            table[u].append((v, cost))

        return table

sol = Solution()
sol.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0)

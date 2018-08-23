import collections
import sys

class BFSSolution:
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
        
        answer = sys.maxsize
        queue = collections.deque()
        queue.append((src, 0))
        level = 0

        while queue:
            # K stops,
            # src is 0 level
            # dst is at most the K + 1 level
            if level > K + 1:
                break
            size = len(queue)

            # check this layer
            for _ in range(size):
                vertex, cost = queue.popleft()

                if vertex == dst:
                    answer = min(answer, cost)
                
                for adj_neighbor, adj_price in adj_table[vertex]:
                    new_cost = cost + adj_price
                    if new_cost > answer: # pruning IMPORTANT
                        continue
                    queue.append((adj_neighbor, new_cost))
            
            # finish this layer
            level += 1
        
        return answer if answer != sys.maxsize else -1


def main():
    sol = BFSSolution()
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1
    print(sol.findCheapestPrice(n, flights, src, dst, k))  # 200

    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 0
    print(sol.findCheapestPrice(n, flights, src, dst, k))  # 500

    n = 5
    flights = [[4, 1, 1], [1, 2, 3], [0, 3, 2],
               [0, 4, 10], [3, 1, 1], [1, 4, 3]]
    src = 2
    dst = 1
    k = 1
    print(sol.findCheapestPrice(n, flights, src, dst, k))  # -1


if __name__ == '__main__':
    main()

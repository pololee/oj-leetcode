import collections


class Solution:
    """
    @param x: The vertices of the edges
    @param y: The vertices of the edges
    @return: Return the index of barycentre
    """

    def getBarycentre(self, x, y):
        # Write your code here
        adjacent_map = self.build_the_graph(x, y)

        degree, subtree_max, subtree_size, leaves, finalized = self.initiate_states(
            adjacent_map
        )
        num_of_vertices = len(adjacent_map)

        while len(finalized) != num_of_vertices and leaves:
            current = leaves.popleft()
            neighbors = adjacent_map[current]

            for neighbor in neighbors:
                if neighbor in finalized:
                    continue

                degree[neighbor] -= 1
                subtree_max[neighbor] = max(
                    subtree_max[neighbor], subtree_size[current])
                subtree_size[neighbor] += subtree_size[current]

                if degree[neighbor] == 1:
                    leaves.append(neighbor)
                    finalized.add(neighbor)
                    subtree_max[neighbor] = max(
                        subtree_max[neighbor], num_of_vertices - subtree_size[neighbor])

        answer = 0
        maxCount = num_of_vertices + 1
        for node in range(1, num_of_vertices + 1):
            if subtree_max[node] < maxCount:
                maxCount = subtree_max[node]
                answer = node

        return answer

    def build_the_graph(self, x, y):
        adjacent_map = collections.defaultdict(set)
        size = len(x)
        for start, end in zip(x, y):
            adjacent_map[start].add(end)
            adjacent_map[end].add(start)

        return adjacent_map

    def initiate_states(self, adjacent_map):
        num_of_vertices = len(adjacent_map)

        # because vertex start from 1
        degree = [0 for _ in range(num_of_vertices + 1)]
        subtree_max = [0 for _ in range(num_of_vertices + 1)]
        subtree_size = [0 for _ in range(num_of_vertices + 1)]

        leaves = collections.deque()
        finalized = set()
        for vertex in range(1, num_of_vertices + 1):
            degree[vertex] = len(adjacent_map[vertex])
            subtree_size[vertex] = 1

            if degree[vertex] == 1:
                leaves.append(vertex)
                finalized.add(vertex)
                subtree_max[vertex] = num_of_vertices - 1
        return degree, subtree_max, subtree_size, leaves, finalized


def main():
    sol = Solution()
    print(sol.getBarycentre([1], [2]))
    print(sol.getBarycentre([1, 2, 2], [2, 3, 4]))


if __name__ == '__main__':
    main()

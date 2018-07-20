import collections


class DFSTopologicalSorting:
    def __init__(self, num_of_vertices, adjacents):
        self.num_of_vertices = num_of_vertices
        self.adjacents = adjacents

    def topological_sorting(self):
        visited = [False for _ in range(self.num_of_vertices)]
        stack = list()

        for i in range(self.num_of_vertices):
            if not visited[i]:
                self.dfs_topological_sorting(i, visited, stack)

        while stack:
            print(stack.pop(), end=' ')
        print()

    def dfs_topological_sorting(self, vertex, visited, stack):
        if visited[vertex]:
            return

        visited[vertex] = True
        for adjacent in self.adjacents[vertex]:
            if visited[adjacent]:
                continue
            self.dfs_topological_sorting(adjacent, visited, stack)

        stack.append(vertex)


def main():
    num_of_vertices = 6
    adjacents = collections.defaultdict(set)
    adjacents[2].add(3)
    adjacents[3].add(1)
    adjacents[4].add(0)
    adjacents[4].add(1)
    adjacents[5].add(0)
    adjacents[5].add(2)

    sorting = DFSTopologicalSorting(6, adjacents)
    sorting.topological_sorting()  # 5 4 2 3 1 0


if __name__ == '__main__':
    main()

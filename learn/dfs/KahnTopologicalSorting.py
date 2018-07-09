import collections


class KahnTopologicalSorting:
    def __init__(self, size, adjacents):
        self.size = size
        self.adjacents = adjacents

    def kahn_topological_sorting(self):
        in_degrees = [0 for _ in range(self.size)]

        for i in range(self.size):
            for end in self.adjacents[i]:
                in_degrees[end] += 1

        queue = collections.deque()
        for i in range(self.size):
            if in_degrees[i] == 0:
                queue.append(i)

        output = []
        while queue:
            vertex = queue.popleft()
            output.append(vertex)

            for end in self.adjacents[vertex]:
                in_degrees[end] -= 1
                if in_degrees[end] == 0:
                    queue.append(end)

        if len(output) != self.size:
            print('There exists a cycle in the graph!!!')
        else:
            print(output)


def main():
    size = 6
    adjacents = collections.defaultdict(set)
    adjacents[2].add(3)
    adjacents[3].add(1)
    adjacents[4].add(0)
    adjacents[4].add(1)
    adjacents[5].add(0)
    adjacents[5].add(2)

    sorting = KahnTopologicalSorting(size, adjacents)
    sorting.kahn_topological_sorting()  # 4 5 2 0 3 1


if __name__ == '__main__':
    main()

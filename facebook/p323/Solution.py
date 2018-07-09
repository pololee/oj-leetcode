class Solution:
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        union_find = UnionFind(n)
        num_of_components = n

        for edge in edges:
            a, b = edge

            root_a = union_find.root(a)
            root_b = union_find.root(b)
            if root_a == root_b:
                continue
            union_find.union(root_a, root_b)
            num_of_components -= 1

        return num_of_components


class UnionFind:
    def __init__(self, size):
        self.size = size
        self.parents = [i for i in range(size)]
        self.weights = [1 for i in range(size)]

    def root(self, x):
        if self.parents[x] == x:
            return x

        self.parents[x] = self.parents[self.parents[x]]
        return self.root(self.parents[x])

    def union(self, root_x, root_y):
        if self.weights[root_x] < self.weights[root_y]:
            self.parents[root_x] = root_y
            self.weights[root_y] += self.weights[root_x]
        else:
            self.parents[root_y] = root_x
            self.weights[root_x] += self.weights[root_y]

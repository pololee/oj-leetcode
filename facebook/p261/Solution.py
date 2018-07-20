class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: list[list[int]]
        :rtype boolean
        """
        if n <= 1:
            return True
        if len(edges) != n - 1:
            return False

        union_find = UnionFind(n)
        for edge in edges:
            a, b = edge

            if union_find.find(a, b):
                return False

            union_find.union(a, b)
        return True


class UnionFind:
    def __init__(self, size):
        self.size = size
        self.parents = [i for i in range(size)]

    def root(self, x):
        if self.parents[x] == x:
            return x

        self.parents[x] = self.parents[self.parents[x]]
        return self.root(self.parents[x])

    def find(self, x, y):
        return self.root(x) == self.root(y)

    def union(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)
        self.parents[root_x] = root_y

class UnionFind:
    def __init__(self, size):
        self.size = size
        self.root_ids = [i for i in range(size)]

    def root_recursive(self, x):
        if self.root_ids[x] == x:
            return x

        return self.root_recursive(self.root_ids[x])

    # def root(self, x):
    #     root_id = self.root_ids[x]

    #     while root_id != x:
    #         root_id = self.root_ids[root_id]

    #     return root_id

    # find out if x and y are in the same set
    def find(self, x, y):
        return self.root_recursive(x) == self.root_recursive(y)

    def union(self, x, y):
        root_x = self.root_recursive(x)
        root_y = self.root_recursive(y)
        self.root_ids[root_x] = root_y  # make the x's root point to y's root


class WeightedUnionFind:
    def __init__(self, size):
        self.size = size
        self.root_ids = [i for i in range(size)]
        self.weights = [1 for i in range(size)]

    def root(self, x):
        if self.root_ids[x] == x:
            return x
        return self.root(self.root_ids[x])

    def find(self, x, y):
        return self.root_ids[x] == self.root_ids[y]

    # we make the root of subset having smaller number of elements
    # point to the root of subset having larger number of elements
    def weighted_union(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)

        if self.weights[root_x] < self.weights[root_y]:
            self.root_ids[root_x] = root_y
            self.weights[root_y] += self.weights[root_x]
        else:
            self.root_ids[root_y] = root_x
            self.weights[root_x] += self.weights[root_y]


class WeightedUnionFindWithPathCompression(WeightedUnionFind):
    def root(self, x):
        if self.root_ids[x] == x:
            return x

        # While computing the root of A, set each i to point to its grandparent
        # (thereby halving the path length),
        # where i is the node which comes in between path, while computing root of A.
        self.root_ids[x] = self.root_ids[self.root_ids[x]]
        return self.root(self.root_ids[x])


if __name__ == '__main__':
    union_find = UnionFind(6)
    union_find.union(1, 0)
    union_find.union(0, 2)
    union_find.union(3, 4)
    union_find.union(1, 4)
    print('UnionFind:')
    print(union_find.root_ids)  # 2, 0, 4, 4, 4, 5
    print(union_find.find(1, 4))  # True
    print(union_find.find(3, 5))  # False
    print('\nWeightedUnionFind')
    weighted_union_find = WeightedUnionFind(6)
    weighted_union_find.weighted_union(0, 1)
    weighted_union_find.weighted_union(1, 2)
    weighted_union_find.weighted_union(3, 2)
    print(weighted_union_find.root_ids)  # 0, 0, 0, 0, 4, 5
    print(weighted_union_find.weights)  # 4, 1, 1, 1, 1, 1
    print('\nWeightedUnionFindWithPathCompression')
    weighted_union_find = WeightedUnionFindWithPathCompression(6)
    weighted_union_find.weighted_union(0, 1)
    weighted_union_find.weighted_union(1, 2)
    weighted_union_find.weighted_union(3, 2)
    print(weighted_union_find.root_ids)  # 0, 0, 0, 0, 4, 5
    print(weighted_union_find.weights)  # 4, 1, 1, 1, 1, 1

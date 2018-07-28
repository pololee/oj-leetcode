class UnionFind:
    def __init__(self, size):
        self.root_ids = [i for i in range(size)]
        self.weights = [1 for _ in range(size)]

    def root(self, x):
        if self.root_ids[x] == x:
            return x

        self.root_ids[x] = self.root_ids[self.root_ids[x]]
        return self.root(self.root_ids[x])

    def find(self, x, y):
        return self.root(x) == self.root(y)

    def union(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)

        if root_x == root_y:
            return False

        if self.weights[root_x] < self.weights[root_y]:
            self.root_ids[root_x] = root_y
            self.weights[root_y] += self.weights[root_x]
        else:
            self.root_ids[root_y] = root_x
            self.weights[root_x] += self.weights[root_y]

        return True


class Solution:
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        if not positions or not positions[0]:
            return []

        answer = []
        count = 0
        land = set()
        union_find = UnionFind(m * n)
        for position in positions:
            count += 1
            row, col = position
            idx = row * n + col
            land.add(idx)

            for x, y in self.DIRECTIONS:
                new_row = row + x
                new_col = col + y
                new_idx = new_row * n + new_col

                if new_row < 0 or new_row >= m or new_col < 0 or new_col >= n or new_idx not in land:
                    continue

                if union_find.union(idx, new_idx):
                    count -= 1
            answer.append(count)
        return answer

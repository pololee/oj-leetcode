class UnionFind:
    def __init__(self, grid):
        num_of_ones = 0
        num_of_rows = len(grid)
        num_of_cols = len(grid[0])
        root_ids = [0 for _ in range(num_of_rows * num_of_cols)]
        weights = [0 for _ in range(num_of_rows * num_of_cols)]

        for row in range(num_of_rows):
            for col in range(num_of_cols):
                idx = row * num_of_cols + col
                if grid[row][col] == '1':
                    num_of_ones += 1
                    root_ids[idx] = idx
                    weights[idx] += 1
                else:
                    root_ids[idx] = -1

        self.count = num_of_ones
        self.root_ids = root_ids
        self.weights = weights

    def root(self, x):
        if self.root_ids[x] == -1:
            return -1

        if self.root_ids[x] == x:
            return x

        # path compression
        self.root_ids[x] = self.root_ids[self.root_ids[x]]
        return self.root(self.root_ids[x])

    def find(self, x, y):
        return self.root(x) == self.root(y)

    def union(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)

        if root_x == root_y:
            return

        self.count -= 1
        if self.weights[root_x] < self.weights[root_y]:
            self.root_ids[root_x] = root_y
            self.weights[root_y] += self.weights[root_x]
        else:
            self.root_ids[root_y] = root_x
            self.weights[root_x] += self.weights[root_y]

    def get_count(self):
        return self.count


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        union_find = UnionFind(grid)
        num_of_rows = len(grid)
        num_of_cols = len(grid[0])
        visited_land = set()

        for row in range(num_of_rows):
            for col in range(num_of_cols):
                if grid[row][col] == '1' and (row, col) not in visited_land:
                    visited_land.add((row, col))
                    idx = row * num_of_cols + col

                    if row - 1 >= 0 and grid[row - 1][col] == '1':
                        union_find.union(idx, (row - 1) * num_of_cols + col)

                    if row + 1 < num_of_rows and grid[row + 1][col] == '1':
                        union_find.union(idx, (row + 1) * num_of_cols + col)

                    if col - 1 >= 0 and grid[row][col - 1] == '1':
                        union_find.union(idx, row * num_of_cols + col - 1)

                    if col + 1 < num_of_cols and grid[row][col+1] == '1':
                        union_find.union(idx, row * num_of_cols + col + 1)
        return union_find.get_count()

def main():
    sol = Solution()
    print(sol.numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], [
          "1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))

if __name__ == '__main__':
    main()

import collections


class ImageMatching:
    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def matched_region_count(self, grid1, grid2):
        """
        :grid1 type: [list[int]]
        :grid1 type: [list[int]]
        :rtype int
        """
        if not grid1 or not grid2:
            return 0

        if len(grid1) == 0 or len(grid1[0]) == 0:
            return 0

        if len(grid2) == 0 or len(grid2[0]) == 0:
            return 0

        m1 = len(grid1)
        n1 = len(grid1[0])
        m2 = len(grid2)
        n2 = len(grid2[0])

        count = 0

        for i in range(m1):
            for j in range(n1):
                if grid1[i][j] == 1:
                    region1 = self.bfs(grid1, i, j, m1, n1)
                    if i < m2 and j < n2 and grid2[i][j] == 1:
                        region2 = self.bfs(grid2, i, j, m2, n2)

                        if self.region_equal(region1, region2):
                            count += 1
        return count

    def bfs(self, grid, i, j, m, n):
        region = []
        queue = collections.deque()
        grid[i][j] = 0  # mark this node has been visited
        queue.append((i, j))

        while queue:
            i, j = queue.popleft()
            region.append((i, j))

            for direction in self.DIRECTIONS:
                new_i = i + direction[0]
                new_j = j + direction[1]

                if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n:
                    continue

                if grid[new_i][new_j] != 1:
                    continue

                grid[new_i][new_j] = 0
                queue.append((new_i, new_j))
        return region

    def region_equal(self, region1, region2):
        if len(region1) != len(region2):
            return False

        for i in range(len(region1)):
            if region1[i][0] != region2[i][0] or region1[i][1] != region2[i][1]:
                return False
        return True


def main():
    grid1 = [[1, 1, 1],
             [1, 0, 0],
             [1, 0, 0]]
    grid2 = [[1, 1, 1],
             [1, 0, 0],
             [1, 0, 1]]
    image = ImageMatching()
    print(image.matched_region_count(grid1, grid2))


if __name__ == '__main__':
    main()

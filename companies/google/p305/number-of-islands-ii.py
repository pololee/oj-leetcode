class UnionFind:
    def __init__(self, size):
        self.f = [i for i in range(size)]
        self.weights = [1 for _ in range(size)]

    def root(self, x):
        if self.f[x] == x:
            return x

        self.f[x] = self.root(self.f[x])
        return self.f[x]

    def union(self, x, y):
        a = self.root(x)
        b = self.root(y)

        if a == b:
            return False

        if self.weights[a] < self.weights[b]:
            self.f[a] = b
            self.weights[b] += self.weights[a]
        else:
            self.f[b] = a
            self.weights[a] += self.weights[b]
        return True


class Solution:
    def numIslands2(self, n, m, operators):
        if n <= 0 or m <= 0 or not operators:
            return []

        ans = []
        unionFind = UnionFind(m * n)
        cnt = 0
        land = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for point in operators:
            x = point.x
            y = point.y

            cnt += 1
            idx = x * n + y
            if idx in land:
                ans.append(cnt)
                continue

            land.add(idx)

            for dx, dy in directions:
                xx = x + dx
                yy = y + dy

                if xx < 0 or xx >= m or yy < 0 or yy >= n:
                    continue

                newIdx = xx * n + yy
                if newIdx not in land:
                    continue

                if unionFind.union(idx, newIdx):
                    cnt -= 1
            ans.append(cnt)
        return ans

class UnionFind:
    def __init__(self, n):
        self.f = [-1 for _ in range(n)]
        # f[x] < 0 means x is root and has abs(f[x]) nodes

    def find(self, x):
        if self.f[x] < 0:
            return x

        self.f[x] = self.find(self.f[x])
        return f[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if self.f[a] < self.f[b]:
            self.f[a] += self.f[b]
            self.f[b] = a
        else:
            self.f[b] += self.f[a]
            self.f[a] = b

# Kruskal
# 1. sort all edges by cost
# 2. traverse all the edges, if the edge doesn't cause circle, add the 
#    edge to the spanning tree.
# Use UnionFind to decide whether it will cause circle or not.
class Connection:

    def __init__(self, city1, city2, cost):
        self.city1, self.city2, self.cost = city1, city2, cost


class UnionFind:
    def __init__(self, n):
        self.f = [-1 for _ in range(n)]

    def find(self, x):
        if self.f[x] < 0:
            return x

        self.f[x] = self.find(self.f[x])
        return self.f[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if self.f[a] < self.f[b]:
            self.f[a] += self.f[b]
            self.f[b] = a
        else:
            self.f[b] += self.f[a]
            self.f[a] = b


class Solution:
    # @param {Connection[]} connections given a list of connections
    # include two cities and cost
    # @return {Connection[]} a list of connections from results
    def lowestCost(self, connections):
        # Write your code here
        if not connections:
            return []

        idTable = self.idHash(connections)
        connections = sorted(
            connections, key=lambda c: (c.cost, c.city1, c.city2))
        ufs = UnionFind(len(idTable))
        ans = []

        for c in connections:
            a = ufs.find(idTable[c.city1])
            b = ufs.find(idTable[c.city2])

            if a != b:
                ans.append(c)
                ufs.union(a, b)

        if len(ans) == len(idTable) - 1:
            return ans

        return []

    def idHash(self, connections):
        table = dict()
        count = 0
        for c in connections:
            if c.city1 not in table:
                table[c.city1] = count
                count += 1

            if c.city2 not in table:
                table[c.city2] = count
                count += 1

        return table

# Think about Kahn algorithm
# The result must be 1 or 2
# you can use counter-evidence. If there are 3, then the middle one is the root
# which can get use the minimum height


class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        adjacents = [set() for _ in range(n)]
        for edge in edges:
            p, q = edge
            adjacents[p].add(q)
            adjacents[q].add(p)

        leaves = []
        for i in range(n):
            if len(adjacents[i]) == 1:
                leaves.append(i)

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                for i in adjacents[leaf]:
                    adjacents[i].remove(leaf)
                    if len(adjacents[i]) == 1:
                        new_leaves.append(i)
            leaves = new_leaves

        return leaves

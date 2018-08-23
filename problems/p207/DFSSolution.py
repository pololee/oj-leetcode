import collections


class DFSSolution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses <= 1:
            return True

        adjacents = collections.defaultdict(set)
        for edge in prerequisites:
            start, end = edge
            adjacents[start].add(end)

        visited = [False for _ in range(numCourses)]
        recursion_stack = [False for _ in range(numCourses)]
        for i in range(numCourses):
            if self.dfs_has_cycle(i, visited, recursion_stack, adjacents):
                return True

        return False

    def dfs_has_cycle(self, vertex, visited, recursion_stack, adjacents):
        if recursion_stack[vertex]:
            return True

        if visited[vertex]:
            return False

        visited[vertex] = True
        recursion_stack[vertex] = True
        for adjacent in adjacents[vertex]:
            # even adjacent has been visited, we still has to call this.
            # because it could be in recursion_stack. e.g 2 node, [[1, 0], [0, 1]]
            if self.dfs_has_cycle(adjacent, visited, recursion_stack, adjacents):
                return True

        recursion_stack[vertex] = False
        return False

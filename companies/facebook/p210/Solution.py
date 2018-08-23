import collections


class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adjacents = collections.defaultdict(set)
        in_degrees = [0 for _ in range(numCourses)]

        for edge in prerequisites:
            end, start = edge
            adjacents[start].add(end)
            in_degrees[end] += 1

        queue = collections.deque()
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)

        output = []
        while queue:
            vertex = queue.popleft()
            output.append(vertex)

            for i in adjacents[vertex]:
                in_degrees[i] -= 1
                if in_degrees[i] == 0:
                    queue.append(i)

        return output if len(output) == numCourses else []

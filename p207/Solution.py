import collections

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses <= 1:
            return True
        
        ajacents = collections.defaultdict(set)
        in_degress = [0 for _ in range(numCourses)]
        for edge in prerequisites:
            start, end = edge
            in_degress[end] += 1
            ajacents[start].add(end)
        
        queue = collections.deque()
        for idx, val in enumerate(in_degress):
            if val == 0:
                queue.append(idx)
        
        num_of_visited = 0
        while queue:
            vertex = queue.popleft()
            num_of_visited += 1

            for end_vertext in ajacents[vertex]:
                in_degress[end_vertext] -= 1
                if in_degress[end_vertext] == 0:
                    queue.append(end_vertext)
        
        return num_of_visited == numCourses

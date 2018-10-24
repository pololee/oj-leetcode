from collections import deque


class Solution:
    def printGraph(self, pairs):
        table = dict()
        root = -1

        for employee, manager in pairs:
            if manager not in table:
                table[manager] = set()
            if employee not in table:
                table[employee] = set()
            if employee == manager:
                root = manager
            else:
                table[manager].add(employee)
        
        visited = set()
        queue = deque()
        queue.append(root)
        visited.add(root)
        level = 0
        levelTable = dict()

        while queue:
          size = len(queue)

          for _ in range(size):
            person = queue.popleft()
            levelTable[person] = level

            for x in table[person]:
              if x in visited:
                continue
              queue.append(x)
          
          level += 1
        
        ans = []
        for person in sorted(levelTable.keys()):
          level = levelTable[person]
          if level > 0:
            ans.append("{}|_{}".format('  ' * (level - 1), person))
          else:
            ans.append(str(person))
        return ans

if __name__=='__main__':
  sol = Solution()
  ans = sol.printGraph([[2, 1],[1, 0], [3, 0], [0, 0]])
  print('\n'.join(ans))

import collections


class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        tickets = sorted(tickets, reverse=True)
        table = collections.defaultdict(list)

        for tFrom, tTo in tickets:
            table[tFrom].append(tTo)

        stack = ['JFK']
        ans = []
        while stack:
            curr = stack[-1]
            if table[curr]:
                stack.append(table[curr].pop())
            else:
                ans.append(stack.pop())
        return ans[::-1]

class DfsSolution:
    def findItinerary(self, tickets):
        tickets = sorted(tickets, reverse=True)
        table = collections.defaultdict(list)

        for tFrom, tTo in tickets:
            table[tFrom].append(tTo)

        ans = []
        self.dfs('JFK', table, ans)
        return ans[::-1]

    def dfs(self, curr, table, ans):
        while len(table[curr]) > 0:
            nextDest = table[curr].pop()
            self.dfs(nextDest, table, ans)

        ans.append(curr)

import collections

class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        tickets = sorted(tickets, reverse=True)
        table = collections.defaultdict(list)

        for tfrom, tto in tickets:
            table[tfrom].append(tto)
        
        route = []
        stack = ['JFK']
        while stack:
            while table[stack[-1]]:
                stack.append(table[stack[-1]].pop())
            route.append(stack.pop())
        
        return list(reversed(route))
    
    def findItineraryRecusive(self, tickets):
        tickets = sorted(tickets, reverse=True)
        table = collections.defaultdict(list)

        for tfrom, tto in tickets:
            table[tfrom].append(tto)
        
        route = []
        def visit(airport):
            while table[airport]:
                visit(table[airport].pop())
            route.append(airport)

        visit('JFK')
        return list(reversed(route))

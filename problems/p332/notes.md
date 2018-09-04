Eulerian path

https://www.youtube.com/watch?v=ycRuO-u6rt8
https://www.youtube.com/watch?v=Dx1lpbpSHwI

Also it should help to see how targets is updating at each step, e.g.,

targets = {'JFK': ['D', 'A'], 'A': ['C'], 'B': ['C'], 'C': ['JFK', 'D'], 'D': ['B', 'A']}
route = []
stack = ['JFK']
First point at which we get stuck:

targets = {'JFK': ['D'], 'A': [], 'B': ['C'], 'C': ['JFK', 'D'], 'D': ['B']}
route = []
stack = ['JFK', 'A', 'C', 'D', 'A']
Update route:

targets = {'JFK': ['D'], 'A': [], 'B': ['C'], 'C': ['JFK'], 'D': ['B']}
route = ['A']
stack = ['JFK', 'A', 'C', 'D']
Search forward again until stuck:

targets = {'JFK': [], 'A': [], 'B': [], 'C': [], 'D': []}
route = ['A']
stack = ['JFK', 'A', 'C', 'D', 'B', 'C', 'JFK', 'D']
Update route:

targets = {'JFK': ['D'], 'A': [], 'B': [], 'C': ['JFK'], 'D': []}
route = ['A', 'D', 'JFK', 'C', 'B', 'D', 'C', 'A', 'JFK']
stack = []
Return route in reverse:

route = ['JFK', 'A', 'C', 'D', 'B', 'C', 'JFK', 'D', 'A']
One last thing, it was really confusing in the Python solution to see foo += bar, instead of foo.append(bar). I think the code would be a lot more readable using append? We can also use the more explicit "reversed" instead of [::-1].

```python
from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # get depts -> dests (with dests in reverse sorted order, since we're popping)
        dept_to_dests = defaultdict(list)
        for dept, dest in sorted(tickets, reverse=True):
            dept_to_dests[dept].append(dest)

        route = []
        stack = ['JFK']

        while stack:
            while dept_to_dests[stack[-1]]:
                t_dest = dept_to_dests[stack[-1]].pop()
                stack.append(t_dest)

            route.append(stack.pop())

        return list(reversed(route))
```

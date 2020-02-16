# ### [362\. Design Hit Counter](https://leetcode.com/problems/design-hit-counter/)

# Difficulty: **Medium**


# Design a hit counter which counts the number of hits received in the past 5 minutes.

# Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

# It is possible that several hits arrive roughly at the same time.

# **Example:**

# ```
# HitCounter counter = new HitCounter();

# // hit at timestamp 1.
# counter.hit(1);

# // hit at timestamp 2.
# counter.hit(2);

# // hit at timestamp 3.
# counter.hit(3);

# // get hits at timestamp 4, should return 3.
# counter.getHits(4);

# // hit at timestamp 300.
# counter.hit(300);

# // get hits at timestamp 300, should return 4.
# counter.getHits(300);

# // get hits at timestamp 301, should return 3.
# counter.getHits(301);
# ```

# **Follow up:**
# What if the number of hits per second could be very large? Does your design scale?


# #### Solution

# Language: **Python3**

# ```python3
# class HitCounter:
# ​
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         
# ​
#     def hit(self, timestamp: int) -> None:
#         """
#         Record a hit.
#         @param timestamp - The current timestamp (in seconds granularity).
#         """
#         
# ​
#     def getHits(self, timestamp: int) -> int:
#         """
#         Return the number of hits in the past 5 minutes.
#         @param timestamp - The current timestamp (in seconds granularity).
#         """
#         
# ​
# ​
# # Your HitCounter object will be instantiated and called as such:
# # obj = HitCounter()
# # obj.hit(timestamp)
# # param_2 = obj.getHits(timestamp)
# ```
class HitCounter:
    INTERVAL = 300

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.times = [-1 for _ in range(self.INTERVAL)]
        self.hits = [0 for _ in range(self.INTERVAL)]

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        idx = timestamp % self.INTERVAL

        if self.times[idx] != timestamp:
            self.times[idx] = timestamp
            self.hits[idx] = 1
        else:
            self.hits[idx] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        total = 0
        for i in range(self.INTERVAL):
            if timestamp - self.times[i] < self.INTERVAL:
                total += self.hits[i]
        return total


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

import collections


class Node:
    def __init__(self, timestamp, hits):
        self.timestamp = timestamp
        self.hits = hits


class HitCounter:
    INTERVAL = 300

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.totalHits = 0
        self.queue = collections.deque()

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if not self.queue or self.queue[-1].timestamp != timestamp:
            self.queue.append(Node(timestamp, 1))
        else:
            self.queue[-1].hits += 1

        self.totalHits += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.removeNodes(timestamp)
        return self.totalHits

    def removeNodes(self, timestamp):
        while self.queue and timestamp - self.queue[0].timestamp >= self.INTERVAL:
            node = self.queue.popleft()
            self.totalHits -= node.hits

# ### [295\. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)

# Difficulty: **Hard**


# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

# For example,

# `[2,3,4]`, the median is `3`

# `[2,3]`, the median is `(2 + 3) / 2 = 2.5`

# Design a data structure that supports the following two operations:

# *   void addNum(int num) - Add a integer number from the data stream to the data structure.
# *   double findMedian() - Return the median of all elements so far.

# **Example:**

# ```
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3)
# findMedian() -> 2
# ```

# **Follow up:**

# 1.  If all integer numbers from the stream are between 0 and 100, how would you optimize it?
# 2.  If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?


# #### Solution

import heapq


class MaxheapWrapper:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return other.val < self.val

    def __eq__(self, other):
        return self.val == other.val

    def __gt__(self, other):
        return other.val > self.val


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smallMax = []
        self.largeMin = []
        self.even = True

    def addNum(self, num: int) -> None:
        if self.even:
            wrapper = heapq.heappushpop(self.smallMax, MaxheapWrapper(num))
            heapq.heappush(self.largeMin, wrapper.val)
        else:
            val = heapq.heappushpop(self.largeMin, num)
            heapq.heappush(self.smallMax, MaxheapWrapper(val))

        self.even = not self.even

    def findMedian(self) -> float:
        if not self.smallMax and not self.largeMin:
            return 0.0

        if self.even:
            return (self.smallMax[0].val + self.largeMin[0]) / 2

        return float(self.largeMin[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

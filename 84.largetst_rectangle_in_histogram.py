# [84\. Largest Rectangle in HistogramCopy for Markdown](https://leetcode.com/problems/largest-rectangle-in-histogram/)

# Difficulty: **Hard**


# Given _n_ non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

# ![](https://assets.leetcode.com/uploads/2018/10/12/histogram.png)
# <small style="display: inline;">Above is a histogram where width of each bar is 1, given height = `[2,1,5,6,2,3]`.</small>

# ![](https://assets.leetcode.com/uploads/2018/10/12/histogram_area.png)
# <small style="display: inline;">The largest rectangle is shown in the shaded area, which has area = `10` unit.</small>

# **Example:**

# ```
# Input: [2,1,5,6,2,3]
# Output: 10
# ```


# #### Solution

# Language: **Python3**

from sys import maxsize
from typing import List


class BruteForceSolution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        maxArea = 0

        for i in range(size):
            minHeight = maxsize
            for j in range(i, size):
                minHeight = min(minHeight, heights[j])
                maxArea = max(maxArea, minHeight * (j - i + 1))
        return maxArea


class DivideConquerSolution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        return self.calculateArea(heights, 0, len(heights) - 1)

    def calculateArea(self, heights, start, end):
        if start > end:
            return 0

        minHeightIdx = start
        for i in range(start, end + 1):
            if heights[i] < heights[minHeightIdx]:
                minHeightIdx = i

        return max(
            heights[minHeightIdx] * (end - start + 1),
            self.calculateArea(heights, start, minHeightIdx - 1),
            self.calculateArea(heights, minHeightIdx + 1, end)
        )


class StackSolution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        size = len(heights)
        stackIdx, i = [-1], 0
        maxArea = 0
        while i < size:
            currHeight = heights[i]
            prevMaxHeight = 0 if stackIdx[-1] == -1 else heights[stackIdx[-1]]

            if prevMaxHeight <= currHeight:
                stackIdx.append(i)
                i += 1
            else:
                stackIdx.pop()
                maxArea = max(maxArea, prevMaxHeight * (i - 1 - stackIdx[-1]))

        while stackIdx[-1] != -1:
            idx = stackIdx.pop()
            h = heights[idx]
            maxArea = max(maxArea, h * (size - 1 - stackIdx[-1]))

        return maxArea


class StackSolutionBetter:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        size = len(heights)
        idxStack, i, maxArea = [-1], 0, 0

        while i < size:
            if idxStack[-1] == -1 or heights[i] >= heights[idxStack[-1]]:
                idxStack.append(i)
                i += 1
            else:
                maxHIdx = idxStack.pop()
                maxH = heights[maxHIdx]
                width = i - 1 - idxStack[-1]
                maxArea = max(maxArea, maxH * width)

        while idxStack[-1] != -1:
            maxHIdx = idxStack.pop()
            maxH = heights[maxHIdx]
            width = size - 1 - idxStack[-1]
            maxArea = max(maxArea, maxH * width)

        return maxArea


if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    bf = BruteForceSolution()
    print(bf.largestRectangleArea(heights))
    dc = DivideConquerSolution()
    print(dc.largestRectangleArea(heights))
    ss = StackSolution()
    print(ss.largestRectangleArea(heights))

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        results = list()

        for inter in intervals:
            if inter.end < newInterval.start or inter.start > newInterval.end:
                results.append(inter)
            else:
                newInterval.start = min(newInterval.start, inter.start)
                newInterval.end = max(newInterval.end, inter.end)

        results.append(newInterval)
        results.sort(key=lambda x: x.start)

        return results

    def insert_2(self, intervals, newInterval):
        results = list()

        i = 0
        while i < len(intervals):
            inter = intervals[i]

            if inter.end >= newInterval.start:
                break
            results.append(inter)
            i += 1

        while i < len(intervals):
            inter = intervals[i]

            if inter.start > newInterval.end:
                break

            newInterval.start = min(newInterval.start, inter.start)
            newInterval.end = max(newInterval.end, inter.end)
            i += 1

        results.append(newInterval)

        while i < len(intervals):
            results.append(intervals[i])
            i += 1

        return results


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        if not schedule or not schedule[0]:
            return []

        allIntervals = []
        for interval in schedule:
            allIntervals.append((interval.start, interval.end))

        allIntervals = sorted(allIntervals)
        end = allIntervals[0][1]
        ans = []
        for curr in allIntervals[1:]:
            if curr[0] > end:
                ans.append(Interval(end, curr[0]))
            end = max(end, curr[1])
        return ans


class AnotherSolution:
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        if not schedule:
            return []

        table = dict()
        for employee in schedule:
            for interval in employee:
                table[interval.start] = table.get(interval.start, 0) + 1
                table[interval.end] = table.get(interval.end, 0) - 1

        sortedByTime = sorted(table.items())
        count = 0
        ans = []
        for time, cnt in sortedByTime:
            count += cnt
            if count == 0:
                ans.append(Interval(time, 0))
            elif count > 0 and ans and ans[-1].end == 0:
                ans[-1].end = time

        if ans and ans[-1].end == 0:
            ans.pop()
        return ans

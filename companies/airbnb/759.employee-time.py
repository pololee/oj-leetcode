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
        if not schedule or not schedule[0]:
            return []
        
        table = dict()
        

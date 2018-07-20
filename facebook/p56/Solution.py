class Interval:
    def __init__(self, s = 0, e = 0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: list[Interval]
        :rtype list[Interval]
        """
        if not intervals or len(intervals) < 2:
            return intervals

        start_sorted_intervals = sorted(intervals, key=lambda interval: interval.start)
        current_start = start_sorted_intervals[0].start
        current_end = start_sorted_intervals[0].end
        answer = []
        for interval in start_sorted_intervals[1:]:
            if interval.start > current_end:
                answer.append(Interval(current_start, current_end))
                current_start = interval.start
                current_end = interval.end
            else:
                current_end = max(current_end, interval.end)
        answer.append(Interval(current_start, current_end))
        return answer

if __name__ == '__main__':
    dummy = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
    sol = Solution()
    answer = sol.merge(dummy)
    print([(i.start, i.end) for i in answer])
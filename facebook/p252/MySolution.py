class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class MySolution:
    def can_attend_meetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key=lambda interval: interval.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        
        return True

def main():
    sol = MySolution()
    test1 = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
    print(sol.can_attend_meetings(test1))
    test2 = [Interval(7, 10), Interval(2, 3)]
    print(sol.can_attend_meetings(test2))

if __name__ == '__main__':
    main()
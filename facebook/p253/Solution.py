import collections

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def min_meeting_rooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0

        timeline_rooms = collections.defaultdict(int)
        for interval in intervals:
            timeline_rooms[interval.start] += 1
            timeline_rooms[interval.end] -= 1

        timestamps = sorted(list(timeline_rooms.keys()))

        answer = 0
        rooms = 0
        for timestamp in timestamps:
            rooms += timeline_rooms[timestamp]
            answer = max(answer, rooms)
        
        return answer

class BetterSolution:
    def min_meeting_rooms(self, intervals):
        starts = []
        ends = []

        for inter in intervals:
            starts.append(inter.start)
            ends.append(inter.end)
        
        starts.sort()
        ends.sort()

        answer = 0
        end_i = 0
        for start in starts:
            if start < ends[end_i]:
                answer += 1
            else:
                end_i += 1
        return answer


def main():
    sol = Solution()
    test1 = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
    print(sol.min_meeting_rooms(test1))
    test2 = [Interval(4, 9), Interval(4, 17), Interval(9, 10)]
    print(sol.min_meeting_rooms(test2))
    bsol = BetterSolution()
    print(bsol.min_meeting_rooms(test1))
    print(bsol.min_meeting_rooms(test2))

if __name__ == '__main__':
    main()

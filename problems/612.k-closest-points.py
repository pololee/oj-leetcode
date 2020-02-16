"""
Definition for a point.

"""


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Wrapper:
    def __init__(self, point, dist):
        self.point = point
        self.dist = dist

    def cmp(self, other):
        if self.dist != other.dist:
            return other.dist - self.dist
        if self.point.x != other.point.x:
            return other.point.x - self.point.x

        return other.point.y - self.point.y

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __eq__(self, other):
        return self.cmp(other) == 0

    def __gt__(self, other):
        return self.cmp(other) > 0


import heapq


class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """

    def kClosest(self, points, origin, k):
        # write your code here
        if not points:
            return []
        
        heap = []
        for point in points:
            dist = self.distance(point, origin)
            heapq.heappush(heap, Wrapper(point, dist))

            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []
        for _ in range(len(heap)):
            ans.append(heapq.heappop(heap).point)
        
        ans.reverse()
        return ans

    def distance(self, point, origin):
        return (point.x - origin.x) ** 2 + (point.y - origin.y) ** 2


def main():
    sol = Solution()
    points = [Point(4, 6), Point(4, 7), Point(4, 4), Point(2, 5), Point(1, 1)]
    origin = Point(0, 0)


if __name__ == '__main__':
    main()

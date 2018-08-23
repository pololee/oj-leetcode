import sys


class Solution:
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        total_dist = 0
        delta = sys.maxsize

        for nut in nuts:
            total_dist += (self.distance(nut, tree) * 2)
            delta = min(delta, self.distance(nut, squirrel) - self.distance(nut, tree))
        
        return total_dist + delta

    def distance(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

def main():
    sol = Solution()
    print(sol.minDistance(5, 7, [2, 2], [4, 4], [[3, 0], [2, 5]]))

if __name__ == '__main__':
    main()

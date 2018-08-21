class Interval:
    def __init__(self, start, end, height):
        self.start = start
        self.end = end
        self.height = height


class IntervalSolution:
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        intervals = []
        ans = []
        size = len(positions)
        max_height = 0

        for i in range(size):
            start, length = positions[i]
            end = start + length
            base_height = 0
            for interval in intervals:
                if start < interval.end and end > interval.start:
                    base_height = max(base_height, interval.height)
            
            height = base_height + length
            intervals.append(Interval(start, end, height))
            max_height = max(max_height, height)
            ans.append(max_height)
        
        return ans

def main():
    sol = IntervalSolution()
    print(sol.fallingSquares([[1, 2], [2, 3], [6, 1]]))  # [2, 5, 5]
    print(sol.fallingSquares([[100, 100], [200, 100]]))  # [100, 100]

if __name__ == '__main__':
    main()

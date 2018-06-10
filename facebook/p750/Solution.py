import collections

class Solution:
    def number_of_corner_rectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype int
        """
        if len(grid) <= 1 or len(grid[0]) <= 1:
            return 0
        
        counter = collections.Counter()
        answer = 0

        for row in grid:
            for left, value in enumerate(row):
                if value == 1:
                    for right in range(left + 1, len(row)):
                        if row[right] == 1:
                            answer += counter[left, right]
                            counter[left, right] += 1
        return answer

def main():
    grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    sol = Solution()
    print(sol.number_of_corner_rectangles(grid))

if __name__ == '__main__':
    main()

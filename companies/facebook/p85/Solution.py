class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        max_rectangle = 0
        num_of_rows = len(matrix)
        num_of_cols = len(matrix[0])
        heights = [0 for _ in range(num_of_cols)]

        for i in range(num_of_rows):
            for j in range(num_of_cols):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            current_rectangle = self.max_hist(heights)
            print(heights)
            print(current_rectangle)
            max_rectangle = max(max_rectangle, current_rectangle)

        return max_rectangle

    def max_hist(self, heights):
        asc_height_idx_stack = []
        max_area = 0
        size = len(heights)

        for i in range(size + 1):
            current = heights[i] if i < size else -1
            while asc_height_idx_stack and heights[asc_height_idx_stack[-1]] >= current:
                top = asc_height_idx_stack.pop()

                if asc_height_idx_stack:
                    current_area = heights[top] * (i - asc_height_idx_stack[-1] - 1)
                else:
                    current_area = heights[top] * i
                print(current_area)
                max_area = max(max_area, current_area)

            asc_height_idx_stack.append(i)
        return max_area


def main():
    test = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]

    sol = Solution()
    print(sol.maximalRectangle(test))

if __name__ == '__main__':
    main()

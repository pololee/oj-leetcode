# http://www.cnblogs.com/lichen782/p/leetcode_Largest_Rectangle_in_Histogram.html

class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0

        asc_height_idx_stack = []
        max_area = 0
        size = len(heights)
        for i in range(size + 1):
            current_height = heights[i] if i < size else -1

            while asc_height_idx_stack and current_height <= heights[asc_height_idx_stack[-1]]:
                top = asc_height_idx_stack.pop()

                if asc_height_idx_stack:
                    area_with_top = heights[top] * (i - asc_height_idx_stack[-1] - 1)
                else:
                    # why the hell the width is i
                    # If asc_height_idx_stack is empty, that means
                    # heights[top] is the "lowest" bar before heights[i] bar
                    # from 0 to i (excluding i), the width is i + 1 - 1
                    area_with_top = heights[top] * i
                max_area = max(max_area, area_with_top)
            asc_height_idx_stack.append(i)
        
        return max_area

def main():
    sol = Solution()
    print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))

if __name__ == '__main__':
    main()

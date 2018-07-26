class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        
        size = len(height)
        total_area = 0
        desc_height_idx_stack = []
        idx = 0

        while idx < size:
            current = height[idx]

            if not desc_height_idx_stack or height[desc_height_idx_stack[-1]] >= current:
                desc_height_idx_stack.append(idx)
                idx += 1
            else:
                lowest_idx = desc_height_idx_stack.pop()
                if not desc_height_idx_stack:
                    continue

                lowest_height = height[lowest_idx]
                high_height = min(current, height[desc_height_idx_stack[-1]])
                water_area = (high_height - lowest_height) * (idx - desc_height_idx_stack[-1] - 1)
                total_area += water_area
        return total_area

class SolutionII:
    def trap(self, height):
        left = 0
        right = len(height) - 1

        if left >= right:
            return 0
        
        total_area = 0
        left_height = height[left]
        right_height = height[right]

        while left < right:
            if left_height < right_height:
                left += 1
                if left_height > height[left]:
                    total_area += (left_height - height[left])
                else:
                    left_height = height[left]
            else:
                right -= 1
                if right_height > height[right]:
                    total_area += (right_height - height[right])
                else:
                    right_height = height[right]
        return total_area


def main():
    sol = Solution()
    print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(sol.trap([4,3,2,1,1,5]))

    solii = SolutionII()
    print(solii.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(solii.trap([4, 3, 2, 1, 1, 5]))

if __name__ == '__main__':
    main()

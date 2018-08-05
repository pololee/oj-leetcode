import sys

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        size = len(nums)
        diff = sys.maxsize

        for i in range(2, size):
            remaining_target = target - nums[i]
            cur_diff = self.explore(nums, 0, i-1, remaining_target)

            if abs(cur_diff) < abs(diff):
                diff = cur_diff
        return target - diff
    
    def explore(self, nums, left, right, target):
        """
        return the smallest diff found (target - (nums[i] + nums[j]))
        """
        diff = sys.maxsize

        while left < right:
            cur_sum = nums[left] + nums[right]
            if cur_sum == target:
                return 0
            
            if abs(target - cur_sum) < abs(diff):
                diff = target - cur_sum
            if cur_sum < target:
                left += 1
            else:
                right -= 1
        return diff

def main():
    sol = Solution()
    print(sol.threeSumClosest([-1, 2, 1, -4], 1))

if __name__ == '__main__':
    main()

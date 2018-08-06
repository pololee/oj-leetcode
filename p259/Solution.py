class Solution:
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0

        nums = sorted(nums)
        total = 0
        for i in range(len(nums) - 2):
            total += self.two_sum_smaller(nums, i + 1, target - nums[i])
        return total

    def two_sum_smaller(self, nums, start, target):
        left = start
        right = len(nums) - 1
        total = 0

        while left < right:
            if nums[left] + nums[right] < target:
                total += (right - left)
                left += 1
            else:
                right -= 1
        return total

def main():
    sol = Solution()
    print(sol.threeSumSmaller([-2, 0, 1, 3], 2))

if __name__ == '__main__':
    main()

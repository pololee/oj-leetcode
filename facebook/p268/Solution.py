class Solution:
    def missing_number(self, nums):
        """
        :type nums: list[int]
        :rtype int
        """
        total_sum = (0 + len(nums)) * (len(nums) + 1) // 2
        for i in nums:
            total_sum -= i
        return total_sum

if __name__ == '__main__':
    sol = Solution()
    print(sol.missing_number([3, 0, 1]))
    print(sol.missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))

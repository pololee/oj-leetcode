class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        tmp = list(nums)
        size = len(nums)

        for i in range(size):
            tmp[(i+k) % size] = nums[i]

        for i in range(size):
            nums[i] = tmp[i]

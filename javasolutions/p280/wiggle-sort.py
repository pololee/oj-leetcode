class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """

    def wiggleSort(self, nums):
        # write your code here
        if not nums:
            return

        size = len(nums)
        for i in range(1, size):
            if i % 2 == 1 and nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
            elif i % 2 == 0 and nums[i-1] < nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]

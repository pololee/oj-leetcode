class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        copied = [x for x in nums]
        copied.sort()

        size = len(copied)
        left = (size + 1) // 2 - 1
        right = size - 1

        for i in range(size):
            if i % 2 == 0:
                nums[i] = copied[left]
                left -= 1
            elif i % 2 == 1:
                nums[i] = copied[right]
                right -= 1


# cannot use left start from 0 and right start from (size + 1) // 2
# if failed with [4, 5, 5, 6]

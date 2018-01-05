# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead
        """
        if not nums or len(nums) == 0:
            return

        # shift non-zero values as farward as possible
        position = 0
        for num in nums:
            if num != 0:
                nums[position] = num
                position += 1

        # fill remaining spaces with zero
        while position < len(nums):
            nums[position] = 0
            position += 1


if __name__ == '__main__':
    sol = Solution()
    test = [0, 1, 0, 3, 12]
    sol.moveZeroes(test)
    print(test)

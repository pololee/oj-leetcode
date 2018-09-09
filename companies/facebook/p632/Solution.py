import sys


class Solution:
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        if not nums or len(nums) == 0:
            return []

        flat_nums = []
        for i in range(len(nums)):
            for num in nums[i]:
                flat_nums.append((num, i))

        flat_nums.sort()

        diff = sys.maxsize
        answer = [0, 0]
        right = 0
        table = dict()
        for left in range(len(flat_nums)):
            while right < len(flat_nums) and not self.valid(table, nums):
                group = flat_nums[right][1]
                if group not in table:
                    table[group] = 1
                else:
                    table[group] += 1

                right += 1

            if self.valid(table, nums):
                curDiff = flat_nums[right-1][0] - flat_nums[left][0]
                if curDiff < diff:
                    diff = curDiff
                    answer = [flat_nums[left][0], flat_nums[right-1][0]]

            left_group = flat_nums[left][1]
            if table[left_group] - 1 == 0:
                del table[left_group]
            else:
                table[left_group] -= 1

        return answer

    def valid(self, table, nums):
        return len(table) == len(nums)

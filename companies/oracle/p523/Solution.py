class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        table = dict()
        table[0] = -1
        the_sum = 0

        for idx, num in enumerate(nums):
            the_sum += num

            if k != 0:
                the_sum %= k

            if the_sum not in table:
                table[the_sum] = idx
            elif idx - table[the_sum] > 1:
                return True

        return False

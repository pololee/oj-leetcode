class Solution:
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """

        size = len(nums)
        results = []
        previous = lower - 1
        current = 0

        for i in range(size + 1):
            current = nums[i] if i < size else upper + 1

            if current - previous > 1:
                results.append(
                    self.range(previous + 1, current - 1)
                )
            previous = current
        return results

    def range(self, start, end):
        if start > end:
            return ""
        if start == end:
            return str(start)
        return "{}->{}".format(start, end)

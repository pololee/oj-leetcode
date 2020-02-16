class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        size = len(nums)
        DP = [[False for _ in range(target + 1)]
              for _ in range(size + 1)]
        DP[0][0] = True

        for i in range(1, size + 1):
            DP[i][0] = True

        for j in range(1, target + 1):
            DP[0][j] = False

        for i in range(1, size + 1):
            num = nums[i-1]
            for j in range(1, target + 1):
                DP[i][j] = DP[i-1][j] or DP[i-1][j-num]

        return DP[size][target]

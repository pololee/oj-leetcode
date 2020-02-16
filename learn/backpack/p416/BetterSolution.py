class BetterSolution:
    def canPartition(self, nums):
        if not nums or len(nums) < 2:
            return False
        
        total = sum(nums)
        if total % 2 != 1:
            return False
        
        target = total // 2
        DP = [False for _ in range(target + 1)]
        DP[0] = True

        for num in nums:
            for i in reversed(range(num, target + 1)):
                DP[i] = DP[i] or DP[i - num]
        
        return DP[target]

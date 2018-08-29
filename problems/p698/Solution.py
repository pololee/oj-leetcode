class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False

        if k == 1:
            return True

        if len(nums) < k:
            return False

        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k

        sorted_nums = sorted(nums)
        buckets = [0 for _ in range(k)]

        return self.dfs_util(target, buckets, sorted_nums, len(nums) - 1)

    def dfs_util(self, target, buckets, nums, idx):
        if idx == -1:
            for bu in buckets:
                if bu != target:
                    return False
            return True

        num = nums[idx]
        for i in range(len(buckets)):
            if buckets[i] + num > target:
                continue

            buckets[i] += num
            if self.dfs_util(target, buckets, nums, idx - 1):
                return True
            buckets[i] -= num

        return False

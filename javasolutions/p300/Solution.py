class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        size = len(nums)
        DP = [1 for _ in range(size)]

        for i in range(1, size):
            for j in range(i):
                if nums[j] < nums[i]:
                    DP[i] = max(DP[i], DP[j] + 1)
        
        return max(DP)


def main():
    sol = Solution()
    print(sol.lengthOfLIS([10, 9, 2, 5, 3, 4]))


if __name__ == '__main__':
    main()

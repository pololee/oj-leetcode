class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        size = len(nums)
        length_DP = [1 for _ in range(size)]
        count_DP = [1 for _ in range(size)]

        for i in range(1, size):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length_DP[i] < length_DP[j] + 1:
                        length_DP[i] = length_DP[j] + 1
                        count_DP[i] = count_DP[j]
                    elif length_DP[i] == length_DP[j] + 1:
                        count_DP[i] += count_DP[j]

        max_length = max(length_DP)
        answer = 0
        for i in range(size):
            if length_DP[i] == max_length:
                answer += count_DP[i]
        return answer


def main():
    sol = Solution()
    print(sol.findNumberOfLIS([5, 4, 3, 2]))


if __name__ == '__main__':
    main()

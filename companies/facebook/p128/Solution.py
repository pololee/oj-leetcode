class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums.sort()

        current = 1
        longest = current
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue

            if nums[i] == nums[i-1] + 1:
                current += 1
            else:
                longest = max(longest, current)
                current = 1

        return longest

class BetterSolution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        longest = 0

        for num in nums:
            if num - 1 in nums:
                continue
            
            current_length = 1
            current_num = num
            while current_num + 1 in nums:
                current_length += 1
                current_num += 1
            longest = max(longest, current_length)
        return longest

def main():
    sol = Solution()
    print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
    better_sol = BetterSolution()
    print(better_sol.longestConsecutive([100, 4, 200, 1, 3, 2]))


if __name__ == '__main__':
    main()

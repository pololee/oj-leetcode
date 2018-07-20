class Solution:
    def min_subarray_len(self, s, nums):
        """
        :type s: int
        :type nums: list[int]
        :rtype int
        """
        left = 0
        answer = None
        subarray_sum = 0

        for i in range(len(nums)):
            subarray_sum += nums[i]

            while subarray_sum >= s:
                sub_len = i - left + 1

                if answer is None or answer > sub_len:
                    answer = sub_len

                subarray_sum -= nums[left]
                left += 1
        return 0 if answer is None else answer

if __name__ == '__main__':
    sol = Solution()
    nums = [2, 3, 1, 2, 4, 3]
    s = 7
    print(sol.min_subarray_len(s, nums))

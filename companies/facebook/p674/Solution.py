class Solution:
    def find_length_of_cis(self, nums):
        """
        :type nums: list[int]
        :rtype int
        """
        if not nums:
            return 0
        
        start = 0
        answer = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                answer = max(answer, i - start + 1)
            else:
                answer = max(answer, i - 1 - start + 1)
                start = i
        return answer

if __name__ == '__main__':
    sol = Solution()
    print(sol.find_length_of_cis([2, 2, 2, 2]))
    print(sol.find_length_of_cis([1, 3, 5, 4, 7]))
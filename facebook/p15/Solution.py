class Solution:
    def three_sum(self, nums):
        """
        :type nums: List[int]
        :rtype List[List[int]]
        """
        answer = []
        if not nums: return answer

        nums = sorted(nums)
        for k in range(0, len(nums) - 2):
            if nums[k] > 0: break
            if k > 0 and nums[k] == nums[k-1]: continue
            
            target = 0 - nums[k]
            i = k + 1
            j = len(nums) - 1
            while i < j:
                if nums[i] + nums[j] == target:
                    answer.append([nums[k], nums[i], nums[j]])
                    while i < j and nums[i] == nums[i+1]: i += 1
                    while i < j and nums[j] == nums[j-1]: j -= 1
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] > target:
                    j -= 1
                else:
                    i += 1
        return answer

def main():
    sol = Solution()
    test = [-1, 0, 1, 2, -1, -4]
    print(sol.three_sum(test))

if __name__ == '__main__':
    main()

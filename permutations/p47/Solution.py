class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort() # very important
        results = []
        used = [False for _ in range(len(nums))]
        self.backtrack(nums, [], results, used)
        return results
    
    def backtrack(self, nums, sofar, results, used):
        if len(sofar) == len(nums):
            results.append(list(sofar))
        else:
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i-1] == nums[i] and not used[i-1]:
                    # if the value are the same, they should be used together or not used together
                    # i.e. if previous one is not used, then don't use current one
                    continue
                used[i] = True
                sofar.append(nums[i])
                self.backtrack(nums, sofar, results, used)
                used[i] = False
                sofar.pop()

def main():
    sol = Solution()
    print(sol.permuteUnique([1, 1, 2]))

if __name__ == '__main__':
    main()

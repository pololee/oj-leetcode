class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        results = []
        # self.backtrack(nums, [], results)
        used = [False for _ in range(len(nums))]
        self.backtrack_with_used(nums, [], results, used)
        # self.backtrack_inplace(nums, 0, results)
        return results

    def backtrack(self, nums, sofar, results):
        if len(sofar) == len(nums):
            results.append(list(sofar))
        else:
            for num in nums:
                if num not in sofar:
                    sofar.append(num)
                    self.backtrack(nums, sofar, results)
                    sofar.pop()

    def backtrack_with_used(self, nums, sofar, results, used):
        if len(sofar) == len(nums):
            results.append(list(sofar))
        else:
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    sofar.append(nums[i])
                    self.backtrack_with_used(nums, sofar, results, used)
                    used[i] = False
                    sofar.pop()

    # permute num[begin..end]
    # invariant: num[0..begin-1] have been fixed/permuted
    def backtrack_inplace(self, nums, begin, results):
        if begin >= len(nums):
            results.append(list(nums))
        else:
            for i in range(begin, len(nums)):
                # swap
                nums[begin], nums[i] = nums[i], nums[begin]
                self.backtrack_inplace(nums, begin + 1, results)
                # reset
                nums[begin], nums[i] = nums[i], nums[begin]


def main():
    sol = Solution()
    print(sol.permute([1, 2, 3]))


if __name__ == '__main__':
    main()

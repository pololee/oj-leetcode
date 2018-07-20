class Solution:
    def subsets(self, nums):
        """
        :nums type: list[int]
        :rtype list[list[int]]
        """
        if not nums:
            return []

        answer = []
        # self.recursive_subsets(nums, 0, [], answer)
        self.backtrack_subsets(answer, [], nums, 0)
        return answer

    def recursive_subsets(self, nums, start, path, answer):
        answer.append(path)

        for i in range(start, len(nums)):
            self.recursive_subsets(nums, i + 1, path + [nums[i]], answer)

    def backtrack_subsets(self, answer, path, nums, start):
        answer.append(path.copy())
        for i in range(start, len(nums)):
            path.append(nums[i])
            self.backtrack_subsets(answer, path, nums, i + 1)
            path.pop()


if __name__ == '__main__':
    sol = Solution()
    test = [1, 2, 3]
    print(sol.subsets(test))

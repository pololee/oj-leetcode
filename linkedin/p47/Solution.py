import collections


class Solution:
    def permute_unique(self, nums):
        """
        :type nums: list[int]
        :rtype list[list[int]]
        """
        if not nums:
            return []
        num_frequency = collections.Counter(nums)
        answers = []
        self.backtrack_permute([], len(nums), num_frequency, answers)
        return answers

    def backtrack_permute(self, so_far, size_of_nums, num_frequency, answers):
        if len(so_far) == size_of_nums:
            answers.append(so_far.copy())
        else:
            for num, frequency in num_frequency.items():
                if frequency > 0:
                    num_frequency[num] -= 1
                    so_far.append(num)
                    self.backtrack_permute(
                        so_far, size_of_nums, num_frequency, answers
                    )
                    num_frequency[num] += 1
                    so_far.pop()


class AnotherSolution:
    def permute_unique(self, nums):
        sorted_nums = sorted(nums)
        answers = []
        used = [False for _ in range(len(nums))]
        self.backtrack_permute(sorted_nums, [], used, answers)
        return answers

    def backtrack_permute(self, nums, so_far, used, answers):
        if len(so_far) == len(nums):
            answers.append(so_far.copy())
        else:
            for i in range(len(nums)):
                if used[i]:
                    continue
                elif i > 0 and nums[i-1] == nums[i] and not used[i-1]:
                    continue

                used[i] = True
                so_far.append(nums[i])
                self.backtrack_permute(nums, so_far, used, answers)
                used[i] = False
                so_far.pop()


if __name__ == '__main__':
    sol = Solution()
    test = [1, 1, 2]
    print(sol.permute_unique(test))
    another_so = AnotherSolution()
    print(another_so.permute_unique(test))

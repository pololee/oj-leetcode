import collections

class Solution:
    def subsets_with_dup(self, nums):
        """
        :nums type: list[int]
        :rtype list[list[int]]
        """
        if not nums:
            return []

        answer = []
        sorted_nums = sorted(nums)
        self.backtrack_subsets(answer, [], sorted_nums, 0)
        return answer

    def backtrack_subsets(self, answer, path, nums, start):
        answer.append(path.copy())

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            self.backtrack_subsets(answer, path, nums, i + 1)
            path.pop()

    # We can treat duplicate element as a spacial element. For example, if we have duplicate elements(5, 5),
    # instead of treating them as two elements that are duplicate, we can treat it as one special element 5,
    # but this element has more than two choices: you can either NOT put it into the subset,
    # or put ONE 5 into the subset,
    # or put TWO 5s into the subset. Therefore, we are given an array(a1, a2, a3, ..., an)
    # with each of them appearing(k1, k2, k3, ..., kn) times, the number of subset is (k1+1)(k2+1)...(kn+1).
    # We can easily see how to write down all the subsets similar to the approach above.
    def iterative_subsets(self, nums):
        answers = []
        answers.append([])

        for num, frequency in collections.Counter(nums).items():
            size_of_answers_for_now = len(answers)
            for i in range(size_of_answers_for_now):
                for j in range(1, frequency + 1):
                    answers.append(answers[i] + [num] * j)

        return answers


if __name__ == '__main__':
    sol = Solution()
    test = [2, 1, 2]
    print(sol.subsets_with_dup(test))
    print(sol.iterative_subsets(test))

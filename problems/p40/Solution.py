class Solution:
    def combination_sum_2(self, candidates, target):
        """
        :candidates type: list[int]
        :target type: int
        :rtype list[list[int]]
        """
        answers = []
        self.backtrack([], target, sorted(candidates), 0, answers)
        return answers

    def backtrack(self, so_far, remain, candidates, start, answers):
        if remain < 0:
            return
        elif remain == 0:
            answers.append(so_far.copy())
        else:
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    continue
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                so_far.append(candidates[i])
                self.backtrack(so_far, remain -
                               candidates[i], candidates, i + 1, answers)
                so_far.pop()


if __name__ == '__main__':
    sol = Solution()
    print(sol.combination_sum_2([10, 1, 2, 7, 6, 1, 5], 8))

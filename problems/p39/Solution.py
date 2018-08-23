class Solution:
    def combination_sum(self, candidates, target):
        """
        :candidates type: list[int]
        :target type: int
        :rtype list[list[int]]
        """
        answers = []
        self.backtrack_combination_sum([], target, candidates, 0, answers)
        return answers

    def backtrack_combination_sum(self, so_far, remain, candidates, start, answers):
        if remain <  0:
            return
        elif remain == 0:
            answers.append(so_far.copy())
        else:
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue
                so_far.append(candidates[i])
                self.backtrack_combination_sum(so_far, remain - candidates[i], candidates, i, answers)
                so_far.pop()


if __name__ == '__main__':
    sol = Solution()
    candidates = [2, 3, 5]
    target = 9
    print(sol.combination_sum(candidates, target))
    candidates = [2, 3, 6, 7]
    target = 7
    print(sol.combination_sum(candidates, target))

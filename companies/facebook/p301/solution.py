class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s:
            return [""]

        left_rem, right_rem = self.misplaced_parentheses(s)
        results = set()
        self.backtrack(
            s, 0, 0, 0, left_rem, right_rem, [], results
        )

        return list(results)

    def misplaced_parentheses(self, s):
        left, right = 0, 0

        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                right = right + 1 if left == 0 else right
                left = left - 1 if left > 0 else left

        return (left, right)

    def backtrack(self, s, index, left_cnt, right_cnt, left_rem, right_rem, expr, results):
        if index == len(s):
            if left_rem == 0 and right_rem == 0:
                results.add("".join(expr))
            return

        # Discard the current
        if s[index] == '(' and left_rem > 0:
            self.backtrack(s,
                           index + 1,
                           left_cnt,
                           right_cnt,
                           left_rem - 1,
                           right_rem,
                           expr,
                           results)
        elif s[index] == ')' and right_rem > 0:
            self.backtrack(s,
                           index + 1,
                           left_cnt,
                           right_cnt,
                           left_rem,
                           right_rem - 1,
                           expr,
                           results)

        # consider the current
        expr.append(s[index])
        if s[index] not in ['(', ')']:
            self.backtrack(s,
                           index + 1,
                           left_cnt,
                           right_cnt,
                           left_rem,
                           right_rem,
                           expr,
                           results)
        elif s[index] == '(':
            self.backtrack(s,
                           index + 1,
                           left_cnt + 1,
                           right_cnt,
                           left_rem,
                           right_rem,
                           expr,
                           results)
        elif s[index] == ')' and left_cnt > right_cnt:
            self.backtrack(s,
                           index + 1,
                           left_cnt,
                           right_cnt + 1,
                           left_rem,
                           right_rem,
                           expr,
                           results)
        expr.pop()

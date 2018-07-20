# Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

# Note: The input string may contain letters other than the parentheses ( and ).

# Examples:
# "()())()" -> ["()()()", "(())()"]
# "(a)())()" -> ["(a)()()", "(a())()"]
# ")(" -> [""]

from collections import deque

class BFSSolution:
    def removeInvalidParentheses(self, s):
        """
        BFS solution:
        0 level, the original string
        1 level, remove one '(' or ')' from the original string, which gives several substring
        2 level, remove one '(' or ')' from one of the above substring, which gives several substring
        ...
        On each level, pick a string from the set, and check whether it is valid or not.
        If on a certain level, we found a valid case, there is no need to go to furher level!!!

        To avoid duplicate answers, when generate the substrings, we only pick unqiues

        :type s: str
        :rtype: List[str]
        """
        results = []

        if not s:
            return [s]

        visited = {s} # create a set. sets are bags of unique values
        queue = deque([s])
        str_is_valid = False

        # DON'T reset str_is_valid.
        # Because the question requires you to `Remove the minimum number of invalid parentheses`
        # which means, if you found a str is valid, then there is no need to go to next level, i.e.
        # remove more chars from the str to get a valid case.
        while queue:
            str_to_check = queue.popleft()

            if self.is_valid(str_to_check):
                results.append(str_to_check)
                str_is_valid = True

            if str_is_valid:
                continue

            for index, ch in enumerate(str_to_check):
                if ch not in ['(', ')']:
                    continue

                substr = str_to_check[:index] + str_to_check[index + 1:]
                if substr not in visited:
                    queue.append(substr)
                    visited.add(substr)

        return results

    def is_valid(self, input_str):
        count = 0

        for ch in input_str:
            if ch == '(':
                count += 1

            if ch == ')':
                count -= 1

            if count < 0:
                return False

        return count == 0


if __name__ == '__main__':
    sol = BFSSolution()
    test = "(a)())()"
    answer = sol.removeInvalidParenthesesBFS(test)
    print(answer)

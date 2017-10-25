# https://leetcode.com/problems/regular-expression-matching/description/

# 10. Regular Expression Matching
# Implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true

class RecursionSolution:
    def is_match(self, text, pattern):
        """
        :type text: str
        :type pattern: str
        :rtype bool
        """
        print('text: {text}, pattern: {pattern}'.format(text = text, pattern = pattern))

        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.is_match(text, pattern[2:])) or (first_match and self.is_match(text[1:], pattern))
        else:
            return first_match and self.is_match(text[1:], pattern[1:])

# dp_state[i][j]: is True if text[0..i-1] matches pattern[0..j-1]
# 
# The dp_state induction of dp_state[i][j]
# 1. text[i-1] == pattern[j-1]
#    dp_state[i][j] = dp_state[i-1][j-1]
# 2. pattern[j-1] == '.'
#    dp_state[i][j] = dp_state[i-1][j-1]
# 3. pattern[j-1] == '*'
#    two sub conditions
#    1. text[i-1] == pattern[j-2] || pattern[j-2] == '.'
#       dp_state[i][j] = dp_state[i][j-2] || dp_state[i-1][j]
#         dp_state[i][j-2] means pattern[j-2] and the '*' (pattern[j-1]) counts as empty
#         dp_state[i-1][j] means pattern[j-2] and the '*' (pattern[j-1]) counts as one or multiple 
#    2. none of the equal satifised
#       in this case, pattern[j-2] and the '*' (pattern[j-1]) counts as empty
#       dp_state[i][j] = dp_state[i][j-2]
class DPSolution:
    def is_match(self, text, pattern):
        """
        :type text: str
        :type pattern: str
        :rtype bool
        """
        textLength = len(text)
        patternLength = len(pattern)
        # the reason we need length + 1
        # because we need to handle empty text and empty pattern
        dp_state = [ [False] * (patternLength + 1) for _ in range(textLength + 1) ]

        # empty text matches empty pattern
        dp_state[0][0] = True

        # dp_state[i][0] = False for i in range(1, textLength + 1)
        # because non-empty text does not match empty pattern
        for j in range(1, patternLength + 1):
            if pattern[j-1] == '*':
                dp_state[0][j] = dp_state[0][j-2]

        for i in range(1, textLength + 1):
            for j in range(1, patternLength + 1):
                if pattern[j-1] in (text[i - 1], '.'):
                    dp_state[i][j] = dp_state[i-1][j-1]
                elif pattern[j-1] == '*':
                    if pattern[j-2] in (text[i - 1], '.'):
                        dp_state[i][j] = dp_state[i-1][j] or dp_state[i][j-2]
                    else:
                        dp_state[i][j] = dp_state[i][j-2]

        print(dp_state)

        return dp_state[textLength][patternLength]


def main():
    # sol = RecursionSolution()
    # sol.is_match("aa", ".*")

    dp_sol = DPSolution()
    print(dp_sol.is_match("aa", ".*"))
    print(dp_sol.is_match("aa", "aa"))
    print(dp_sol.is_match("aa", "a"))
    print(dp_sol.is_match("", ".*"))

if __name__ == '__main__':
    main()
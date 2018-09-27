import collections


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ""

        ttable = collections.Counter(t)

        answer = ""
        minLength = len(s) + 1
        right = 0
        stable = collections.defaultdict(int)
        for left in range(len(s)):
            while right < len(s) and not self.valid(stable, ttable):
                stable[s[right]] += 1
                right += 1

            # after the above while loop
            # right should not be included in the answer, since it either
            # >= len(s) or makes the valid false
            if self.valid(stable, ttable):
                if right - left < minLength:
                    minLength = right - left
                    answer = s[left:right]
            stable[s[left]] -= 1

        return answer

    # how to define valid
    # all the keys in ttable exist in stable
    # the value in stable should >= value n ttable
    def valid(self, stable, ttable):
        for key, value in ttable.items():
            if key not in stable:
                return False
            elif stable[key] < value:
                return False
        return True

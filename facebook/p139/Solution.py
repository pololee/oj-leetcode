class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        size = len(s)
        # DP[i] represent
        # in s, from 0, length of i substring satisfy wordBreak or not
        # e.g in s, from 0 to i - 1 substring satisfy wordBreak or not
        DP = [False for _ in range(size + 1)]
        DP[0] = True

        for length in range(1, size + 1):
            for i in range(length):
                if DP[i] and s[i:length] in wordDict:
                    DP[length] = True
        return DP[size]

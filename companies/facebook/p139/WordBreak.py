class WordBreak:
    def wordBreak(self, s, dict):
        # write your code here
        if not s:
            return True

        size = len(s)
        canSegment = [False for _ in range(size + 1)]
        canSegment[0] = True

        maxWordLen = self.maxWordLen(dict)
        wordDict = set(dict)

        for length in range(1, size + 1):
            for lastWordLen in range(1, 1 + min(length, maxWordLen)):
                if not canSegment[length - lastWordLen]:
                    continue

                word = s[length - lastWordLen: length]
                if word in wordDict:
                    canSegment[length] = True
                    break

        return canSegment[size]

    def maxWordLen(self, dict):
        maxLen = 0
        for word in dict:
            maxLen = max(maxLen, len(word))

        return maxLen

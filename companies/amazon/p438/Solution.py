import collections


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s:
            return []
        if len(s) < len(p):
            return []

        pTable = collections.Counter(p)
        sTable = dict()

        sSize = len(s)
        pSize = len(p)
        matchedChars = 0
        answer = []
        j = 0

        for i in range(sSize):
            if s[i] not in pTable:
                continue

            while j < i + pSize and j < sSize:
                if s[j] not in sTable:
                    sTable[s[j]] = 1
                else:
                    sTable[s[j]] += 1

                if s[j] in pTable and sTable[s[j]] == pTable[s[j]]:
                    matchedChars += 1
                j += 1

            if j - i == pSize and matchedChars == len(pTable):
                answer.append(i)

            if sTable[s[i]] == pTable[s[i]]:
                matchedChars -= 1
            sTable[s[i]] -= 1

        return answer

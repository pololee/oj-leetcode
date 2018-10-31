from collections import Counter


class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """

    def minWindow(self, source, target):
        # write your code here
        targetTable = Counter(target)
        size = len(source)

        j = 0
        matched = 0
        matchTable = dict()
        ans = ""
        ansLen = size + 1

        for i in range(size):
            while j < size and matched < len(targetTable):
                ch = source[j]

                matchTable[ch] = matchTable.get(ch, 0) + 1
                if ch in targetTable and targetTable[ch] == matchTable[ch]:
                    matched += 1

                j += 1

            if matched == len(targetTable):
                if j - i < ansLen:
                    ansLen = j - i
                    ans = source[i:j]

            leftCh = source[i]
            matchTable[leftCh] -= 1
            if leftCh in targetTable and matchTable[leftCh] < targetTable[leftCh]:
                matched -= 1

        return ans

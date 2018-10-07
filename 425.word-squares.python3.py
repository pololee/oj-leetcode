class Solution:
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        if not words:
            return []

        wordLen = len(words[0])
        prefixTable = self.prefixHash(words)
        ans = []
        self.dfs(0, wordLen, [], ans, prefixTable)
        return ans

    def dfs(self, idxToAdd, wordLen, squares, ans, prefixTable):
        if idxToAdd == wordLen:
            ans.append(list(squares))
            return

        prefix = []
        for i in range(idxToAdd):
            prefix.append(squares[i][idxToAdd])
        prefix = ''.join(prefix)

        for word in prefixTable.get(prefix, []):
            if not self.ableToAdd(idxToAdd, wordLen, word, squares, prefixTable):
                continue

            squares.append(word)
            self.dfs(idxToAdd + 1, wordLen, squares, ans, prefixTable)
            squares.pop()

    def ableToAdd(self, idxToAdd, wordLen, nextWord, squares, prefixTable):
        for j in range(idxToAdd + 1, wordLen):
            prefix = []
            for i in range(idxToAdd):
                prefix.append(squares[i][j])
            prefix.append(nextWord[j])
            prefix = ''.join(prefix)

            if prefix not in prefixTable:
                return False
        return True

    def prefixHash(self, words):
        table = dict()

        for word in words:
            for i in range(len(word)):
                prefix = word[:i]
                if prefix in table:
                    table[prefix].append(word)
                else:
                    table[prefix] = [word]

        return table


def main():
    test = ["area", "lead", "wall", "lady", "ball"]
    sol = Solution()
    print(sol.wordSquares(test))


if __name__ == '__main__':
    main()

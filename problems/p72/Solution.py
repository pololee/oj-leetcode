#        a       b         c        d
#    +-------+--------+--------+--------+
#    |       |        |        |        |
# a  |   0   |   1    |   2    |    3   |
#    |       |        |        |        |
#    +----------------------------------+
#    |       |        |        |        |
#    |       |        |        |        |
# b  |   1   |   0    |   1    |    2   |
#    |       |        |        |        |
#    +----------------------------------+
#    |       |        |        |        |
#    |       |        |        |        |
# e  |   2   |        |        |        |
#    |       |        |        |        |
#    +----------------------------------+
#    |       |        |        |        |
# f  |   3   |        |        |        |
#    |       |        |        |        |
#    +-------+--------+--------+--------+


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        DP = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # DP[i][j] represent the min distance between word1[0..i-1] and word2[0..j-1]

        for i in range(1, m + 1):
            DP[i][0] = i
        for j in range(1, n + 1):
            DP[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    DP[i][j] = DP[i - 1][j - 1]
                else:
                    DP[i][j] = min(DP[i-1][j-1] + 1,
                                   min(DP[i-1][j] + 1, DP[i][j-1] + 1))
        return DP[m][n]

def main():
    sol = Solution()
    print(sol.minDistance("intention", "execution"))

if __name__ == '__main__':
    main()

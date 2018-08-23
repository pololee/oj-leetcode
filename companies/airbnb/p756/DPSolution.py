import collections


class DPSolution:
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        table = collections.defaultdict(set)
        for string in allowed:
            table[string[-1]].add(string[:2])
        
        N = len(bottom)
        DP = [[[False for _ in range(7)]
                for _ in range(N)]
                for _ in range(N)]
        
        for idx, ch in enumerate(bottom):
            ch_idx = ord(ch) - ord('A')
            DP[N-1][idx][ch_idx] = True
        
        for i in reversed(range(N-1)):
            for j in range(i + 1):
                for k in range(7):
                    ch = chr(ord('A') + k)
                    if ch in table:
                        for base in table[ch]:
                            left_idx = ord(base[0]) - ord('A')
                            right_idx = ord(base[1]) - ord('A')
                            if DP[i+1][j][left_idx] and DP[i+1][j+1][right_idx]:
                                DP[i][j][k] = True
        
        for i in range(7):
            if DP[0][0][i]:
                return True
        return False


def main():
    sol = DPSolution()
    print(sol.pyramidTransition("ABC", ["ABD", "BCE", "DEA", "FFF"]))
    # print(sol.pyramidTransition("XXYX", ["XXX", "XXY", "XYX", "XYY", "YXZ"]))


if __name__ == '__main__':
    main()

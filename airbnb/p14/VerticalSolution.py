class VerticalSolution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        
        size_0 = len(strs[0])
        for i in range(size_0):
            cur_char = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or cur_char != strs[j][i]:
                    return strs[0][0:i]
        return strs[0]


def main():
    sol = VerticalSolution()
    print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
    print(sol.longestCommonPrefix(["dog", "racecar", "car"]))


if __name__ == '__main__':
    main()

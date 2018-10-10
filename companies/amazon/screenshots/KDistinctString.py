class KDistinctString:
    def substrings(self, inputStr, num):
        if not inputStr or num <= 0:
            return []

        size = len(inputStr)
        table = dict()
        answer = set()
        j = 0

        for i in range(size):
            while j < i + num and j < size:
                if inputStr[j] in table:
                    table[inputStr[j]] += 1
                else:
                    table[inputStr[j]] = 1

                j += 1

            if j == i + num and len(table) == num and inputStr[i:i+num] not in table:
                answer.add(inputStr[i:i+num])

            table[inputStr[i]] -= 1
            if table[inputStr[i]] == 0:
                del table[inputStr[i]]

        return list(answer)


def main():
    sol = KDistinctString()
    inputStr = "awaglknagawunagwkwagl"
    num = 4
    print(sol.substrings(inputStr, num))

if __name__ == '__main__':
    main()

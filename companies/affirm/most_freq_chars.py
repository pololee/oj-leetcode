import unittest
import string


class Solution:
    def mostFreqChars(self, words):
        maxTable = dict()
        for ch in string.ascii_lowercase:
            maxTable[ch] = 0

        cntTable = dict()

        for word in words:
            uniqueChars = list(set(word))
            size = len(uniqueChars)

            for i in range(size):
                for j in range(i):
                    x = uniqueChars[i]
                    y = uniqueChars[j]
                    cntTable[(x, y)] = cntTable.get((x, y), 0) + 1
                    cntTable[(y, x)] = cntTable.get((y, x), 0) + 1
                    maxTable[x] = max(maxTable[x], cntTable[(x, y)])
                    maxTable[y] = max(maxTable[y], cntTable[(y, x)])

        ans = dict()
        for key in maxTable:
            if maxTable[key] == 0:
                continue

            ans[key] = list()
            for ch in string.ascii_lowercase:
                if (key, ch) in cntTable and cntTable[(key, ch)] == maxTable[key]:
                    ans[key].append(ch)
        return ans


class SolutionTest(unittest.TestCase):
    def testMostFreqChars(self):
        test = ["abc", "bcd", "cde"]
        sol = Solution()
        expected = {
            'a': ['b', 'c'],
            'b': ['c'],
            'c': ['b', 'd'],
            'd': ['c'],
            'e': ['c', 'd']
        }
        self.assertDictEqual(expected, sol.mostFreqChars(test))

        test = ["abe", "bcc", "cde"]
        expected = {
            'a': ['b', 'e'],
            'b': ['a', 'c', 'e'],
            'c': ['b', 'd', 'e'],
            'd': ['c', 'e'],
            'e': ['a', 'b', 'c', 'd']
        }
        self.assertDictEqual(expected, sol.mostFreqChars(test))



if __name__ == "__main__":
    unittest.main()

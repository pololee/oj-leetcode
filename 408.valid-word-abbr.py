import unittest


class Solution:
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        if not word and not abbr:
            return True
        if not word or not abbr:
            return False
        if len(word) < len(abbr):
            return False

        wordSize = len(word)
        i = 0
        abbrSize = len(abbr)
        j = 0
        while i < wordSize and j < abbrSize:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] > '0' and abbr[j] <= '9':
                start = j
                while j < abbrSize and abbr[j].isdigit():
                    j += 1
                num = int(abbr[start:j])
                i += num
            else:
                return False

        return i == wordSize and j == abbrSize


class SolutionTest(unittest.TestCase):
    sol = Solution()

    def testValid(self):
        self.assertTrue(self.sol.validWordAbbreviation(
            "internationalization",
            "i12iz4n")
        )


if __name__ == '__main__':
    unittest.main()

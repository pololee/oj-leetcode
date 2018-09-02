class Solution:
    TABLE = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        if len(digits) == 1:
            return self.TABLE[digits[0]]

        answer = []
        front = self.letterCombinations(digits[:-1])
        for fr in front:
            for ch in self.TABLE[digits[-1]]:
                answer.append(fr + ch)

        return answer

class Solution:
    CHARS_MAP = ["0", "1", "abc", "def", "ghi",
                 "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        if len(digits) == 1:
            return list(self.CHARS_MAP[int(digits[0])])

        answer = []
        front = self.letterCombinations(digits[:-1])
        for fr in front:
            for ch in self.CHARS_MAP[int(digits[-1])]:
                answer.append(fr + ch)

        return answer

class BfsSolution:
    CHARS_MAP = ["0", "1", "abc", "def", "ghi",
                 "jkl", "mno", "pqrs", "tuv", "wxyz"]
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        results = [""]
        for digit in digits:
            temp = []
            for ch in self.CHARS_MAP[int(digit)]:
                for fr in results:
                    temp.append(fr + ch)
            results = temp
        return results

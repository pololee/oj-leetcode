class Solution:
    TABLE = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        stack = []
        for ch in s:
            if ch in self.TABLE:
                stack.append(ch)
            elif not stack or self.TABLE[stack.pop()] != ch:
                return False

        return len(stack) == 0

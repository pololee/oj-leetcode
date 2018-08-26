class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        ops = []
        nums = []

        size = len(s)
        i = 0

        while i < size:
            ch = s[i]

            if ch.isdigit():
                start = i
                while i + 1 < size and s[i+1].isdigit():
                    i += 1
                nums.append(int(s[start:i+1]))
            elif ch == '(':
                ops.append(ch)
            elif ch == ')':
                while ops and ops[-1] != '(':
                    self.operation(ops, nums)
                ops.pop()
            elif ch in ('+', '-'):
                while ops and self.should_perform_ops(ops[-1], ch):
                    self.operation(ops, nums)
                ops.append(ch)

            i += 1
        while ops:
            self.operation(ops, nums)

        return nums[-1]

    def operation(self, ops, nums):
        operator = ops.pop()
        right = nums.pop()
        left = nums.pop()

        if operator == '+':
            nums.append(left + right)
        elif operator == '-':
            nums.append(left - right)

    def should_perform_ops(self, previous, current):
        if previous == '(':
            return False

        return True

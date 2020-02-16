class Solution:
    def calculate(self, s):
        if not s:
            return 0

        stack = []
        operator = '+'

        i, size = 0, len(s)

        while i < size:
            print("{}, ch: {}".format(i, s[i]))
            ch = s[i]

            if ch == "(":
                exprStart = i
                exprEnd = self.findExprEnd(s, exprStart)
                exprAns = self.calculate(s[exprStart+1:exprEnd])
                self.updateStack(stack, operator, exprAns)

                i = exprEnd + 1
            elif ch.isdigit():
                numStart = i
                numEnd = self.findNumEnd(s, numStart)
                num = int(s[numStart:numEnd + 1])
                self.updateStack(stack, operator, num)

                i = numEnd + 1
            elif ch in ('+', '-', '*', '/'):
                operator = ch
                i += 1
            else:
                i += 1

        ans = 0
        for x in stack:
            ans += x

        return ans

    def findExprEnd(self, s, start):
        cnt, i = 0, start
        while i < len(s):
            if s[i] == "(":
                cnt += 1
            if s[i] == ")":
                cnt -= 1
            if cnt == 0:
                break

            i += 1
        return i

    def findNumEnd(self, s, start):
        i = start
        while i + 1 < len(s) and s[i+1].isdigit():
            i += 1
        return i

    def updateStack(self, stack, operator, value):
        if operator == "+":
            stack.append(value)
        elif operator == "-":
            stack.append(value * -1)
        elif operator == "*":
            stack.append(stack.pop() * value)
        elif operator == "/":
            stack.append(stack.pop() // value)

if __name__ == "__main__":
    sol = Solution()
    print(sol.calculate("-4 + 3 + (5 - 1) * 2"))

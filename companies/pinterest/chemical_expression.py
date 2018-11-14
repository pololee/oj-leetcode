class Solution:
    def parse(self, s):
        if not s:
            return {}

        i = 0
        size = len(s)
        table = {}

        while i < size:
            if s[i].isupper():
                name, i = self.parseName(s, i)
                tmpTable = { name: 1 }
                num = 1
                if i+1 < size and s[i+1].isdigit():
                    num, i = self.parseNumber(s, i+1)
                if name in table:
                    table[name] += num
                else:
                    table[name] = num
            elif s[i] == '(':
                left = i
                i = self.parseBracket(s, left)
                tmpTable = self.parse(s[left + 1:i])
                if i+1 < size and s[i+1].isdigit():
                    num, i = self.parseNumber(s, i + 1)
                    for key in tmpTable:
                        tmpTable[key] *= num
                for key in tmpTable:
                    if key in table:
                        table[key] += tmpTable[key]
                    else:
                        table[key] = tmpTable[key]
            i += 1
        return table

    def parseName(self, s, start):
        i = start
        size = len(s)
        name = [s[i]]

        while i + 1 < size and s[i+1].islower():
            name.append(s[i+1])
            i += 1
        name = ''.join(name)
        return name, i

    def parseNumber(self, s, start):
        i = start
        size = len(s)
        num = int(s[start])

        while i + 1 < size and s[i+1].isdigit():
            num = num * 10 + int(s[i+1])
            i += 1
        return num, i

    def parseBracket(self, s, left):
        size = len(s)
        cnt = 1
        right = left + 1
        while right < size and cnt > 0:
            if s[right] == '(':
                cnt += 1
            elif s[right] == ')':
                cnt -= 1
            right += 1
        return right - 1

sol = Solution()
print(sol.parse("(M3(Aa2(BiC2)Aa)3)")) # {'M': 3, 'Aa': 9, 'Bi': 3, 'C': 6}

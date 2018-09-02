class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [['', 1]]
        num = ''
        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == '[':
                stack.append(['', int(num)])
                num = ''
            elif ch == ']':
                sample, repeatNum = stack.pop()
                stack[-1][0] += sample * repeatNum
            else:
                stack[-1][0] += ch
        return stack[0][0]
    
    def my_stupid_solution(self, s):
        nums = []
        chars = []
        i = 0
        
        while i < len(s):
            if s[i].isdigit():
                x = 0
                while i < len(s) and s[i].isdigit():
                    x = x * 10 + int(s[i])
                    i += 1
                nums.append(x)
            elif s[i] != ']':
                chars.append(s[i])
                i += 1
            else:
                tmp = []
                while chars and chars[-1] != '[':
                    tmp.append(chars.pop())
                
                if chars:
                    chars.pop()
                
                tmp = ''.join(tmp[::-1])
                num = nums.pop()
                for _ in range(num):
                    chars.append(tmp)
                i += 1
        
        return ''.join(chars)

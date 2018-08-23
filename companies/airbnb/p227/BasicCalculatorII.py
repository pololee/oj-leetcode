# Implement a basic calculator to evaluate a simple expression string.

# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

# You may assume that the given expression is always valid.

# Some examples:
# "3+2*2" = 7
# " 3/2 " = 1
# " 3+5 / 2 " = 5
# Note: Do not use the eval built-in library function.

class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        numbers = []
        num = 0
        sign = '+'

        for index, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)

            if ch in ['+', '-', '*', '/'] or index == len(s) - 1:
                if sign == '+':
                    numbers.append(num)
                elif sign == '-':
                    numbers.append(-1 * num)
                elif sign == '/':
                    left_number = numbers.pop()
                    numbers.append(left_number // num)
                elif sign == '*':
                    left_number = numbers.pop()
                    numbers.append(left_number * num)
                sign = ch
                num = 0
        
        answer = 0
        for number in numbers:
            answer += number
        
        return answer

if __name__ == '__main__':
    sol = Solution()
    answer = sol.calculate("3+5 / 2")
    print(answer)
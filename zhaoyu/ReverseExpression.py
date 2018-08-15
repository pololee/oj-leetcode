class ReverseExpression:
    def reverse(self, string):
        """
        :type string: str
        :rtype str
        """
        if not string:
            return ''
        
        nums = []
        operators = []

        buffer = string[0]
        for i in range(1, len(string)):
            ch = string[i]

            if ch.isdigit() or ch == '.':
                buffer += ch
            elif string[i-1].isdigit():
                nums.append(buffer)
                buffer = ""
                operators.append(ch)
            else:
                buffer += ch
        nums.append(buffer)
        print(nums)
        print(operators)
        answer = ""
        for i in reversed(range(len(operators))):
            answer = answer + nums[i+1] + operators[i]
        answer += nums[0]

        return answer

def main():
    express = ReverseExpression()
    print(express.reverse('1*2.4+9.6-23.89'))
    print(express.reverse('1*2.4+-9.6-23.89'))
    print(express.reverse('-1*2.4+9.6-23.89'))

if __name__ == '__main__':
    main()

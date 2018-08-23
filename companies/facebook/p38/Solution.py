class Solution:
    def count_and_say(self, n):
        """
        :n type: int
        :rtype str
        """
        if n <= 0:
            return ''

        answer = '1'
        for _ in range(n - 1):
            current_char = answer[0]
            counter = 1
            temp_str = ''

            for i in range(1, len(answer)):
                if current_char == answer[i]:
                    counter += 1
                else:
                    temp_str = temp_str + str(counter) + current_char
                    counter = 1
                    current_char = answer[i]
            temp_str = temp_str + str(counter) + current_char
            answer = temp_str
        return answer

def main():
    sol = Solution()
    print(sol.count_and_say(1))
    print(sol.count_and_say(2))
    print(sol.count_and_say(3))
    print(sol.count_and_say(4))
    print(sol.count_and_say(5))
    print(sol.count_and_say(6))
    print(sol.count_and_say(7))

if __name__ == '__main__':
    main()

class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype str
        """
        if not num1 or not num2:
            return ''

        length1 = len(num1)
        length2 = len(num2)
        product_array = [ 0 for _ in range(length1 + length2)]
        for i in range(length1 - 1, -1, -1):
            for j in range(length2 - 1, -1, -1):
                multiplied = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1 # check the image in the same directory
                current_sum = multiplied + product_array[p2]

                product_array[p1] += current_sum // 10
                product_array[p2] = current_sum % 10

        answer = ''
        for num in product_array:
            if not (len(answer) == 0 and num == 0):
                answer += str(num)
        return answer or '0'

    def multiply_easy_understand(self, num1, num2):
        if not num1 or not num2:
            return ''

        length1 = len(num1)
        length2 = len(num2)
        product_array = [0 for _ in range(length1 + length2)]
        for i in range(length1 - 1, -1, -1):
            for j in range(length2 - 1, -1, -1):
                product_array[i + j + 1] += int(num1[i]) * int(num2[j])

        carry = 0
        for i in range(length1 + length2 - 1, -1, -1):
            tmp = product_array[i] + carry
            product_array[i] = tmp % 10
            carry = tmp // 10

        answer = ''
        for num in product_array:
            if not (len(answer) == 0 and num == 0):
                answer += str(num)
        return answer or '0'

if __name__ == '__main__':
    sol = Solution()
    print(sol.multiply_easy_understand('0', '0'))
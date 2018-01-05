class Solution:
    def add_binary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_i = len(a) - 1
        b_i = len(b) - 1
        carry = 0
        answer = ''

        while a_i >= 0 and b_i >= 0:
            bit_sum = self.to_int(a[a_i]) + self.to_int(b[b_i]) + carry
            answer = "{}{}".format(bit_sum % 2, answer)
            carry = bit_sum // 2

            a_i -= 1
            b_i -= 1

        while a_i >= 0:
            bit_sum = self.to_int(a[a_i]) + carry
            answer = "{}{}".format(bit_sum % 2, answer)
            carry = bit_sum // 2

            a_i -= 1

        while b_i >= 0:
            bit_sum = self.to_int(b[b_i]) + carry
            answer = "{}{}".format(bit_sum % 2, answer)
            carry = bit_sum // 2

            b_i -= 1

        if carry > 0:
            answer = "{}{}".format(carry, answer)

        return answer

    def to_int(self, ch):
        if ch == '1':
            return 1

        if ch == '0':
            return 0

def main():
    sol = Solution()
    print(sol.add_binary('11', '1'))

if __name__ == '__main__':
    main()
class Solution:
    """
    @param n: an integer
    @return:  the factorial of n
    """

    def factorial(self, n):
        # write your code here
        if n == 0:
            return 1

        ans = [1]

        for x in range(2, n + 1):
            self.multiply(ans, x)

        return ''.join(reversed([str(i) for i in ans]))

    def multiply(self, ans, x):
        carry = 0
        size = len(ans)

        for i in range(size):
            prod = ans[i] * x + carry
            ans[i] = prod % 10
            carry = prod // 10

        while carry != 0:
            ans.append(carry % 10)
            carry //= 10

def main():
    sol = Solution()
    print(sol.factorial(20))
    print("2432902008176640000")

if __name__ == '__main__':
    main()

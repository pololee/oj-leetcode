class Solution:
    MOD_BASE = 10 ** 9 + 7

    def num_of_decodings(self, s):
        if not s or s[0] == '0': return 0

        length = len(s)
        dp = [0] * (length + 1)
        dp[0] = 1
        dp[1] = 9 if s[0] == '*' else 1

        for i in range(2, length + 1):
            single_digit_multiplier = self.single_digit_case_multiplier(
                s[i - 1])
            dp[i] = (
                dp[i] + dp[i - 1] * single_digit_multiplier) % self.MOD_BASE

            double_digits_multiplier = self.double_digits_case_multiplier(
                s[i - 2], s[i - 1])
            dp[i] = (dp[i] + dp[i - 2] * double_digits_multiplier) % self.MOD_BASE

        return dp[length]

    def single_digit_case_multiplier(self, ch):
        if ch == '*':
            return 9
        elif ch == '0':
            return 0
        else:
            return 1

    def double_digits_case_multiplier(self, first_ch, second_ch):
        if first_ch == '0':
            return 0

        if first_ch == '1':
            if second_ch == '*':
                return 9
            else:
                return 1

        if first_ch == '2':
            if second_ch == '*':
                return 6
            elif second_ch > '6':
                return 0
            else:
                return 1

        if first_ch == '*':
            if second_ch == '*':
                return 15  # 9 + 6
            elif second_ch > '6':
                return 1
            else:
                return 2

        return 0

def main():
    sol = Solution()
    print(sol.num_of_decodings("*")) # expect 9
    print(sol.num_of_decodings("1*")) # expect 18

if __name__ == '__main__':
    main()

class Solution:
    def num_decodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 整理总结corner case：
        # XY可以解码的条件是：9<XY<=26
        # Y可以单独解码的条件是：Y != '0'
        if not s or s[0] == '0' : return 0

        # Now the length of s is >= 0
        # and it doesn't start with '0'
        # dp[n] represents given a string of length n, the number of
        # decode ways
        length = len(s)
        dp = [0] * (length + 1)
        # just to make it work. hard to explain why it's 1 of length 0 string
        # it contradicts with the first if check.
        dp[0] = 1
        dp[1] = 1

        for i in range(2, length + 1):
            single_digit = int(s[i-1:i])
            double_digits = int(s[i-2:i])

            if single_digit >= 1 and single_digit <= 9:
                dp[i] += dp[i-1]
            if double_digits >= 10 and double_digits <= 26:
                dp[i] += dp[i-2]
        
        return dp[length]

def main():
    sol = Solution()
    test = "12"
    print(sol.num_decodings(test)) # expect 2

if __name__ == '__main__':
    main()

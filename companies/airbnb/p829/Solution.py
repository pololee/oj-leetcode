class Solution:
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 0:
            return 0
        
        answer = 0
        # (x + 1) + (x + 2) + ... + (x + k) = N
        # k^2 + 2 kx + k = 2N
        k = 1
        while k * k + k < 2 * N:
            if 2 * N % k == 0:
                y = 2 * N // k - k - 1
                if y >= 0 and y % 2 == 0:
                    answer += 1
            k += 1
        return answer

def main():
    sol = Solution()
    print(sol.consecutiveNumbersSum(5))

if __name__ == '__main__':
    main()

class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        DP = dict()
        count = 0

        for i in range(size):
            start = i
            end = i
            while start >= 0 and end < size:
                if start == end:
                    DP[(start, end)] = True
                    count += 1
                elif s[start] == s[end] and DP[(start + 1, end - 1)]:
                    DP[(start, end)] = True
                    count += 1
                else:
                    DP[(start, end)] = False
                start -= 1
                end += 1

            start = i
            end = i + 1
            while start >= 0 and end < size:
                if s[start] != s[end]:
                    DP[(start, end)] = False
                elif end - start == 1 or DP[(start + 1, end - 1)]:
                    DP[(start, end)] = True
                    count += 1
                else:
                    DP[(start, end)] = False
                start -= 1
                end += 1

        return count

def main():
    sol = Solution()
    print(sol.countSubstrings('abc'))
    print(sol.countSubstrings('aaa'))

if __name__ == '__main__':
    main()

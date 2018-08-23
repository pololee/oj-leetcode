class Solution:
    def min_cut(self, s):
        """
        :type s: str
        :rtype int
        """
        if not s:
            return 0

        size = len(s)
        # Prepare DP
        # dp_min_cuts store the data: min cuts needed at the index of i in the string
        # at index 0, only one char, so the dp_min_cuts[0] = 0
        # at index 1, two chars, so the dp_min_cuts[1] = 1
        # ...
        # at index n - 1, n chars, so the dp_min_cuts[n-1] = n -1
        dp_min_cuts = [i for i in range(size)]

        for mid in range(1, size):
            # odd length
            start = mid
            end = mid
            while start >= 0 and end < size and s[start] == s[end]:
                # if start == 0, it means from start to end, it is a palindrome
                # so at index of end, the min_cuts is 0
                # If start != 0, it means from start to end, it is a palindrome
                # start to end is one cut + the min_cuts at index of start - 1
                # The sum is the new min_cuts
                new_min_cuts = 0 if start == 0 else dp_min_cuts[start - 1] + 1
                dp_min_cuts[end] = min(new_min_cuts, dp_min_cuts[end])
                start -= 1
                end += 1

            # even length
            start = mid - 1
            end = mid
            while start >= 0 and end < size and s[start] == s[end]:
                new_min_cuts = 0 if start == 0 else dp_min_cuts[start - 1] + 1
                dp_min_cuts[end] = min(new_min_cuts, dp_min_cuts[end])
                start -= 1
                end += 1

        return dp_min_cuts[size - 1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.min_cut('aab'))
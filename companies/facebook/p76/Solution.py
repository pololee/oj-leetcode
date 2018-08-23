from collections import Counter

class Solution:
    def min_window(self, s, t):
        """
        :s type: str
        :t type: str
        """
        if not s or len(s) < len(t):
            return ''

        char_counts = Counter(t) # which gives the frequency of each char in t
        min_start = 0
        min_sub_len = len(s) + 1 # min_start and min_sub_len gives us the way to get the sub str
        start = 0
        counter = len(t)

        for end, ch in enumerate(s):
            if ch in char_counts:
                char_counts[ch] -= 1
                # char_counts[ch] >= 0 means this ch is counted as a effective char towarads the
                # string t. if it < 0, it should have any effect on counter
                if char_counts[ch] >= 0:
                    counter -= 1
            while counter == 0:
                # counter == 0 means we have found a sub_str in s that satifies the requirement.
                if end - start + 1 < min_sub_len:
                    min_start = start
                    min_sub_len = end - start + 1

                # try to shrink the window by moving the start
                # note, move start may change the counter because when we move the start,
                # the char may "effectively" be counted towards the final window
                start_char = s[start]
                if start_char in char_counts:
                    char_counts[start_char] += 1
                    if char_counts[start_char] > 0:
                        counter += 1
                start += 1

        return '' if min_sub_len > len(s) else s[min_start:min_start + min_sub_len]

if __name__ == '__main__':
    sol = Solution()
    print(sol.min_window('ADOBECODEBANC', 'ABC')) # expect BANC
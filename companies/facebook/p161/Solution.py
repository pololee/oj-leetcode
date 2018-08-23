class Solution:
    def is_one_edit_distance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype str
        """
        if len(s) == len(t):
            return self.is_replace_one(s, t)
        elif len(s) + 1 == len(t):
            return self.is_insert_one(t, s)
        elif len(s) == len(t) + 1:
            return self.is_insert_one(s, t)
        else:
            return False

    def is_replace_one(self, s, t):
        diff_count = 0
        for i in range(len(s)):
            if s[i] != t[i]:
                diff_count += 1
            if diff_count > 1:
                return False

        return diff_count == 1

    def is_insert_one(self, long_str, short_str):
        i = 0
        j = 0
        while i < len(long_str) and j < len(short_str):
            if long_str[i] == short_str[j]:
                i += 1
                j += 1
            else:
                if i != j:
                    return False
                i += 1
        return True

def main():
    sol = Solution()
    print(sol.is_one_edit_distance('aaa', 'aab'))
    print(sol.is_one_edit_distance('a', 'ba'))

if __name__ == "__main__":
    main()

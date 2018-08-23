class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_to_t_mapping = {}
        t_to_s_mapping = {}
        size = len(s)

        for i in range(size):
            s_ch = s[i]
            t_ch = t[i]

            if s_ch in s_to_t_mapping and t_ch not in t_to_s_mapping:
                return False
            
            if s_ch not in s_to_t_mapping and t_ch in t_to_s_mapping:
                return False
            
            if s_ch in s_to_t_mapping and t_ch in t_to_s_mapping:
                if s_to_t_mapping[s_ch] != t_ch or t_to_s_mapping[t_ch] != s_ch:
                    return False
            else:
                s_to_t_mapping[s_ch] = t_ch
                t_to_s_mapping[t_ch] = s_ch

        return True

def main():
    sol = Solution()
    print(sol.isIsomorphic('egg', 'add'))
    print(sol.isIsomorphic('foo', 'bar'))

if __name__ == '__main__':
    main()   


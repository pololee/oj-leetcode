class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        
        prefix = strs[0]
        for item in strs:
            prefix = self.common_prefix(prefix, item)
            if not prefix:
                return ''
        
        return prefix
    
    def common_prefix(self, a, b):
        i = 0
        prefix = ''
        while i < len(a) and i < len(b):
            if a[i] == b[i]:
                prefix += a[i]
            else:
                break
            i += 1
        return prefix

def main():
    sol = Solution()
    print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
    print(sol.longestCommonPrefix(["dog", "racecar", "car"]))

if __name__ == '__main__':
    main()

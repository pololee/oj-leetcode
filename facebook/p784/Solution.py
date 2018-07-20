class Solution:
    def letter_case_permutation(self, s):
        """
        :type s: str
        :rtype list[str]
        """
        if not s:
            return []

        results = []
        self.permutation_recusive(s, 0, results)
        return results
    
    def permutation_recusive(self, s, i, results):
        if i == len(s):
            results.append(s)
            return
        
        self.permutation_recusive(s, i + 1, results)

        if s[i].isalpha():
            ch = s[i].lower() if s[i].isupper() else s[i].upper()
            new_s = s[:i] + ch + s[i+1:]
            self.permutation_recusive(new_s, i + 1, results)
        

if __name__ == '__main__':
    sol = Solution()
    print(sol.letter_case_permutation('a1b1'))
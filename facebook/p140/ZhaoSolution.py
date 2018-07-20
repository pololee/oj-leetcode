class ZhaoSolution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict = set(wordDict)
        solutions_map = dict()
        return self.work_break_dfs(s, wordDict, solutions_map)
    
    def work_break_dfs(self, s, wordDict, solutions_map):
        if s in solutions_map:
            return solutions_map[s]
        
        if not s:
            return ['']
        
        solutions = []
        for word in wordDict:
            if s.startswith(word):
                substr_solutions = self.work_break_dfs(
                    s[len(word):], wordDict, solutions_map
                )
                for sub_sol in substr_solutions:
                    if sub_sol:
                        solutions.append(word + ' ' + sub_sol)
                    else:
                        solutions.append(word)
        solutions_map[s] = solutions
        return solutions

def main():
    sol = ZhaoSolution()
    s = 'catsanddog'
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print(sol.wordBreak(s, wordDict))
    s = 'pineapplepenapple'
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    print(sol.wordBreak(s, wordDict))

if __name__ == '__main__':
    main()

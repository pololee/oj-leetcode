class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        return self.work_break_dfs(s, wordDict, dict())

    def work_break_dfs(self, s, wordDict, results_map):
        if s in results_map:
            return results_map[s]
        
        if not s:
            return ['']
        
        results = []
        for word in wordDict:
            if s.startswith(word):
                solution = str(word)
                the_other_part_results = self.work_break_dfs(
                    s[len(word):],
                    wordDict,
                    results_map
                )
                for other_part_result in the_other_part_results:
                    if not other_part_result: # empty string
                        results.append(solution)
                    else:
                        solution = solution + ' ' + other_part_result
                        results.append(solution)
        results_map[s] = results
        return results

def main():
    sol = Solution()
    s = 'catsanddog'
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print(sol.wordBreak(s, wordDict))

if __name__ == '__main__':
    main()

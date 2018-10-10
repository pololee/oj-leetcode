class WordBreakII:
    def wordBreak(self, s, wordDict):
        done = dict()

        self.dfs(s, set(wordDict), done)
        return done[s]
    

    def dfs(self, s, wordDict, done):
        if len(s) == 0:
            return [""]
        
        if s in done:
            return done[s]
        
        results = []
        if s in wordDict:
            results.append(s)
        
        for i in range(1, len(s)):
            word = s[:i]
            if word not in wordDict:
                continue
            
            suffix = s[i:]
            segmentations = self.dfs(suffix, wordDict, done)
            for seg in segmentations:
                results.append("{} {}".format(word, seg))
        
        done[s] = results
        return results

# ### [126\. Word Ladder II](https://leetcode.com/problems/word-ladder-ii/)

# Difficulty: **Hard**


# Given two words (_beginWord_ and _endWord_), and a dictionary's word list, find all shortest transformation sequence(s) from _beginWord_ to _endWord_, such that:

# 1.  Only one letter can be changed at a time
# 2.  Each transformed word must exist in the word list. Note that _beginWord_ is _not_ a transformed word.

# **Note:**

# *   Return an empty list if there is no such transformation sequence.
# *   All words have the same length.
# *   All words contain only lowercase alphabetic characters.
# *   You may assume no duplicates in the word list.
# *   You may assume _beginWord_ and _endWord_ are non-empty and are not the same.

# **Example 1:**

# ```
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# Output:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]
# ```

# **Example 2:**

# ```
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

# Output: []

# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
# ```


# #### Solution


# ------------------------------------------------------------------------------------------
# High level explainantion
# - find the neighbor word: replace a char and check if the new word in the wordlist or not
# - Given the neighbor word, use BFS to find the shortest path distance
#   when doing this, build the adjTable and distanceTable
# - use DFS to find all the shortest paths
#
# Trick:
# This trick is very important because it can reduce a lot of useless DFS calls.
#
# We don't want to dfs all the neighbors. We only want to go to the neighbor we know we could
# reach the end and on the shortest path.
# So in the BFS step,
# - if we start from the beginWord, we use find neighbor words to list all the neighbors
# but when record the edge, we should record neighbor -> beginWord, not beginWord -> neighbor.
# In BFS, we would stop when we reach endWord.
# Because we record neighbor -> beginWord, then adjTable[endWord] only list all the neighbors
# that have shortest path to beginWord. I know it's confusing, but pay attention to the code,
# and try to understand this.
# Since adjTable[beginWord] has nothing, adjTable[endWord] record all the neighbors that
# have shortest path to beginWord. So in DFS, we start from endWord
# - if we start from the endWord, we use find neighbor words to list all the neighbors.
# But when record the edge, same thing, we should record neighbor -> endWord
# In DFS, we should start from beginWord


from typing import List
import string
import collections

# BFS start from beginWord, DFS start from endWord


class SolutionA:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)

        if endWord not in wordList:
            return []

        adjTable, disTable = self.bfsFromBeginWord(
            beginWord, endWord, wordList
        )
        ans = []
        self.dfsFromEndWord(beginWord, [endWord], ans, adjTable, disTable)
        return ans

    def getNextWords(self, word, wordList):
        ans = []

        for i in range(len(word)):
            left = word[:i]
            right = word[i+1:]

            for ch in string.ascii_lowercase:
                if ch == word[i]:
                    continue
                newWord = "{}{}{}".format(left, ch, right)
                if newWord in wordList:
                    ans.append(newWord)
        return ans

    def bfsFromBeginWord(self, beginWord, endWord, wordList):
        adjTable = collections.defaultdict(set)
        disTable = {beginWord: 0}

        queue = collections.deque()
        queue.append(beginWord)
        while queue:
            word = queue.popleft()

            if word == endWord:
                break

            for x in self.getNextWords(word, wordList):
                adjTable[x].add(word)  # word <- x, instead of word -> x

                if x in disTable:
                    continue

                disTable[x] = disTable[word] + 1
                queue.append(x)

        return (adjTable, disTable)

    def dfsFromEndWord(self, beginWord, sofar, ans, adjTable, disTable):
        if len(sofar) > 1 and sofar[-1] == beginWord:
            ans.append(list(reversed(sofar)))
            return

        last = sofar[-1]
        for x in adjTable[sofar[-1]]:
            if disTable[x] != disTable[last] - 1:
                continue

            sofar.append(x)
            self.dfsFromEndWord(beginWord, sofar, ans, adjTable, disTable)
            sofar.pop()


class SolutionB:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)

        if endWord not in wordList:
            return []

        wordList.add(beginWord) # otherwise, there is no way in the bfs to reach beginWord
        adjTable, disTable = self.bfsFromEndWord(beginWord, endWord, wordList)
        ans = []
        self.dfsFromBeginWord(endWord, [beginWord], ans, adjTable, disTable)
        return ans

    def getNextWords(self, word, wordList):
        ans = []

        for i in range(len(word)):
            left = word[:i]
            right = word[i+1:]

            for ch in string.ascii_lowercase:
                if ch == word[i]:
                    continue

                newWord = "{}{}{}".format(left, ch, right)
                if newWord in wordList:
                    ans.append(newWord)
        return ans

    def bfsFromEndWord(self, beginWord, endWord, wordList):
        adjTable = collections.defaultdict(set)
        disTable = {endWord: 0}

        queue = collections.deque()
        queue.append(endWord)
        while queue:
            word = queue.popleft()

            if word == beginWord:
                break

            for x in self.getNextWords(word, wordList):
                adjTable[x].add(word)  # x <- word, not word -> x

                if x in disTable:
                    continue
                disTable[x] = disTable[word] + 1
                queue.append(x)

        return (adjTable, disTable)

    def dfsFromBeginWord(self, endWord, sofar, ans, adjTable, disTable):
        if len(sofar) > 1 and sofar[-1] == endWord:
            ans.append(sofar.copy())
            return

        last = sofar[-1]
        for x in adjTable[last]:
            if disTable[x] != disTable[last] - 1:
                continue

            sofar.append(x)
            self.dfsFromBeginWord(endWord, sofar, ans, adjTable, disTable)
            sofar.pop()


if __name__ == "__main__":
    sol = SolutionA()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(sol.findLadders(beginWord, endWord, wordList))

    solB = SolutionB()
    print(solB.findLadders(beginWord, endWord, wordList))

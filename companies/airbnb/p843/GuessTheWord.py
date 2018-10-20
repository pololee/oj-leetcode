# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

# If there are cntMatches exact matches(value and position) between our guess and the secret word, 
# those words do not share cntMatches exact matches with the guess are invalid.
#
# For example, secret = "abcdef", guess = "abcghi", cntMatches = 3.
# Obviously, a valid candidate must start with "abc".
# Thus, countSameChars(candidate, guess) has to return 3 exactly.


import random


class Solution:
    WORDLENGTH = 6

    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        size = len(wordlist)
        guessIdx = random.randrange(size)
        guessWord = wordlist[guessIdx]
        matchCnt = master.guess(guessWord)
        if matchCnt == self.WORDLENGTH:
            return

        matchGroupByCnt = self.preProcessWordlist(wordlist)
        possible = matchGroupByCnt[guessIdx][matchCnt]

        for _ in range(9):  # the above guess used once, only 9 guesses left
            guessIdx = random.choice(list(possible))
            guessWord = wordlist[guessIdx]
            matchCnt = master.guess(guessWord)
            if matchCnt == self.WORDLENGTH:
                return

            currPossible = matchGroupByCnt[guessIdx][matchCnt]
            possible = possible.intersection(currPossible) # the common elements from last possible and curr possible

    def preProcessWordlist(self, wordlist):
        size = len(wordlist)
        pairMatchCnt = [[0 for _ in range(size)] for _ in range(size)]
        # pairMatchCnt[i][j]
        # represent the value of self.matchCnt(wordlist[i], wordlist[j])
        for i in range(size):
            pairMatchCnt[i][i] = self.WORDLENGTH
            for j in range(i):
                cnt = self.matchCnt(wordlist[j], wordlist[i])
                pairMatchCnt[i][j] = cnt
                pairMatchCnt[j][i] = cnt

        matchGroupByCnt = [[set() for _ in range(self.WORDLENGTH + 1)]
                           for _ in range(size)]
        for i in range(size):
            for j in range(size):
                cnt = pairMatchCnt[i][j]
                matchGroupByCnt[i][cnt].add(j)
        return matchGroupByCnt

    def matchCnt(self, x, y):
        cnt = 0
        for i in range(len(x)):
            if x[i] == y[i]:
                cnt += 1
        return cnt

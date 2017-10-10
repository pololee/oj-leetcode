class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words or maxWidth <= 0:
            return []

        answer = []
        start = 0
        totalWordsLength = 0
        for index, word in enumerate(words):
            if len(word) > maxWidth:
                return answer

            currentWordsWidthIfAdded = totalWordsLength + len(word) + (index - start)
            if currentWordsWidthIfAdded <= maxWidth:
                totalWordsLength += len(word)
            else:
                answer.append(self.buildLine(words, maxWidth, start, index - 1, totalWordsLength))
                start = index
                totalWordsLength = len(words[index])
        
        answer.append(self.buildLine(words, maxWidth, start, len(words) - 1, totalWordsLength, True))
        return answer

    def buildLine(self, words, maxWidth, start, end, totalWordsLength, isLastLine=False):
        if start < 0 or end > len(words) or start > end:
            return ""

        line = words[start]
        numOfWords = end - start + 1
        if numOfWords == 1 or isLastLine:
            for i in range(start + 1, end + 1):
                line += " " + words[i]
            
            spacesToAppend = maxWidth - totalWordsLength - (numOfWords - 1)
            line += " " * spacesToAppend
            return line

        space = (maxWidth - totalWordsLength) // (numOfWords - 1)
        extra = (maxWidth - totalWordsLength) % (numOfWords - 1)
        for i in range(start + 1, end + 1):
            line += " " * space

            if extra > 0:
                line += " "
                extra -= 1
            
            line += words[i]
        
        return line

if __name__ == '__main__':
    sol = Solution()
    test = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    answer = sol.fullJustify(test, maxWidth)
    print("\n".join(answer))


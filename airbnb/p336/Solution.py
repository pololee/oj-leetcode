class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        if not words:
            return []

        # The words are unique as said in the question
        # we can set up a table to achieve O(1) look up time
        table = {}
        for idx, word in enumerate(words):
            table[word] = idx

        results = []
        for idx, word in enumerate(words):
            length = len(word)

            for i in range(length + 1):
                left_sub = word[:i]
                right_sub = word[i:]

                if self.is_palindrome(left_sub):
                    reversed_right_sub = right_sub[::-1]
                    if reversed_right_sub in table and table[reversed_right_sub] != idx:
                        pair = [table[reversed_right_sub], idx]
                        results.append(pair)
                
                if len(right_sub) != 0 and self.is_palindrome(right_sub):
                    reversed_left_sub = left_sub[::-1]
                    if reversed_left_sub in table and table[reversed_left_sub] != idx:
                        pair = [idx, table[reversed_left_sub]]
                        results.append(pair)
        return results
    def is_palindrome(self, word):
        if not word:
            return True

        left = 0
        right = len(word) - 1

        while left <= right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1

        return True

def main():
    sol = Solution()
    test = ["abcd", "dcba", "lls", "s", "sssll"]
    print(sol.palindromePairs(test))
    test = ["bat", "tab", "cat"]
    print(sol.palindromePairs(test))
    test = ['a', '']
    print(sol.palindromePairs(test))

if __name__ == '__main__':
    main()

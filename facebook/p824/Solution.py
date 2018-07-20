class Solution:
    VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    def to_goat_latin(self, S):
        """
        :type S: str
        :rtype str
        """
        words = S.split(' ')
        answer = []
        for idx, word in enumerate(words):
            answer.append(self.convert_word(word, idx + 1))

        return ' '.join(answer)

    def convert_word(self, word, word_idx):
        surfix = 'a' * word_idx

        if word[0] in self.VOWELS:
            return word + 'ma' + surfix

        return word[1:] + word[0]+ 'ma' + surfix

if __name__ == '__main__':
    test = 'I speak Goat Latin'
    expected = 'Imaa peaksmaaa oatGmaaaa atinLmaaaaa'
    sol = Solution()
    assert(sol.to_goat_latin(test) == expected)
    test2 = 'The quick brown fox jumped over the lazy dog'
    expected2 = 'heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa'
    assert(sol.to_goat_latin(test2) == expected2)
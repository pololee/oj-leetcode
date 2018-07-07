import string
import collections

class Solution:
    ALPHA_LOWERCASE = set(string.ascii_lowercase)

    def ladder_length(self, begin_word, end_word, word_list):
        """
        :type begin_word: str
        :type end_word: str
        :type word_list: list[str]
        :rtype int
        """
        word_list = set(word_list)
        if end_word not in word_list:
            return 0
        if begin_word in word_list:
            word_list.remove(begin_word)

        to_visit = collections.deque()
        self.add_neighbors(begin_word, to_visit, word_list)

        level = 1 # the begin_word is level 1
        while to_visit:
            level += 1
            size_of_to_visit = len(to_visit)
            for _ in range(size_of_to_visit):
                word = to_visit.popleft()
                if end_word == word:
                    return level
                else:
                    neighbors = []
                    self.add_neighbors(word, neighbors, word_list)
                    to_visit.extend(neighbors)
        return 0
    
    def add_neighbors(self, word, neighbors, word_list):
        if not word_list:
            return

        if word in word_list:
            word_list.remove(word)
        
        for i in range(len(word)):
            curr_char = word[i]
            for char in self.ALPHA_LOWERCASE:
                if char == curr_char:
                    continue
                potential_word = word[:i] + char + word[i+1:]
                if potential_word in word_list:
                    neighbors.append(potential_word)
                    word_list.remove(potential_word)

if __name__ == '__main__':
    sol = Solution()
    begin_word = "hit"
    end_word = "cog"
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(sol.ladder_length(begin_word, end_word, word_list))
    word_list = ["hot", "dot", "dog", "lot", "log"]
    print(sol.ladder_length(begin_word, end_word, word_list))
    print(sol.ladder_length('a', 'c', ['a', 'b', 'c']))

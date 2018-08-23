import collections


class SolutionII:
    def ladder_length(self, begin_word, end_word, word_list):
        word_list = set(word_list)
        if end_word not in word_list:
            return 0

        to_visit = collections.deque()
        self.add_neighbors(begin_word, to_visit, word_list)

        level = 1
        while to_visit:
            level += 1
            size_of_to_visit = len(to_visit)
            for _ in range(size_of_to_visit):
                word = to_visit.popleft()

                if word == end_word:
                    return level
                else:
                    neighbors = []
                    self.add_neighbors(word, neighbors, word_list)
                    to_visit.extend(neighbors)
        return 0

    def add_neighbors(self, word, neighbors, wordlist):
        if not wordlist:
            return

        for each_word in wordlist:
            if self.words_diff_by_one(each_word, word):
                neighbors.append(each_word)

        for neighbor_word in neighbors:
            wordlist.remove(neighbor_word)

    def words_diff_by_one(self, a, b):
        if a == b:
            return False
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
            if diff > 1:
                return False
        return True if diff == 1 else False


if __name__ == '__main__':
    sol = SolutionII()
    print(sol.ladder_length('hit', 'cog', [
          "hot", "dot", "dog", "lot", "log", "cog"]))
    print(sol.ladder_length('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]))

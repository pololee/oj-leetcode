import collections


class SolutionII:
    NUM_OF_LETTERS = 26
    A_CODE = ord('a')

    def groupAnagrams(self, words):
        """
        :words: list[str]
        :rtype list[list[str]]
        """
        if not words:
            return []

        table = collections.defaultdict(set)
        for word in words:
            char_counts_string = self.compute_char_count(word)
            table[char_counts_string].add(word)
        
        return list(table.values())

    def compute_char_count(self, word):
        char_counts = [0 for _ in range(self.NUM_OF_LETTERS)]

        for ch in word:
            idx = ord(ch) - self.A_CODE
            char_counts[idx] += 1
        
        return '#'.join(map(str, char_counts))

def main():
    sol = SolutionII()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

if __name__ == '__main__':
    main()

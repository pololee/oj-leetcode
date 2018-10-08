import heapq


class Wrapper:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        else:
            return self.freq < other.freq


class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        table = dict()
        for word in words:
            table[word] = table.get(word, 0) + 1

        heap = []
        for word, freq in table.items():
            heapq.heappush(heap, Wrapper(freq, word))
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []
        while heap:
            item = heapq.heappop(heap)
            ans.append(item.word)

        return ans[::-1]

def main():
    sol = Solution()
    print(sol.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"],
                           3))
    print(sol.topKFrequent(["aaa", "aa", "a"],
                           2))

if __name__ == '__main__':
    main()

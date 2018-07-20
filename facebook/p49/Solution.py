from collections import defaultdict

class Solution:
    def group_anagrams(self, strs):
        """
        :type strs: list[str]
        :rtype list[list[str]]
        """
        if not strs:
            return []

        table = defaultdict(list)
        for string in strs:
            key = tuple(sorted(string))
            table[key].append(string)

        return list(table.values())

if __name__ == '__main__':
    test = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sol = Solution()
    print(sol.group_anagrams(test))

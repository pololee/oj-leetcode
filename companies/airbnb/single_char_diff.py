class Solution:
    def only_one_diff(self, words):
        if not words:
            return True
        
        table = dict()
        for word in words:
            for i in range(len(word)):
                sub_word = "{}_{}".format(word[:i], word[i+1:])
                if sub_word in table:
                    return True
                table[sub_word] = True
        
        return False

        def only_one_diff_with_trie(self, words):
            # left -> right direction to 
            # https://1o24bbs.com/t/topic/12551/4

class TrieNode:
    def __init__(self):
        self.word = None
        self.children = dict()

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch in node:
                node = node.children[ch]
            else:
                new_node = TrieNode()
                node.children[ch] = new_node
                node = new_node
        node.word = word

if __name__ == "__main__":
    sol = Solution()
    print(sol.only_one_diff(["abc", "xyz", "abd"]))
    print(sol.only_one_diff(["abc", "xyz", "def"]))
    print(sol.only_one_diff(["abcd", "bbbb", "abxd", "cccc"]))

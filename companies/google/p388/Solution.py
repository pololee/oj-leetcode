class Node:
    def __init__(self, length, level, is_file):
        self.length = length
        self.level = level
        self.is_file = is_file


class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        if not input:
            return 0
        
        words = input.split("\n")
        nodes = list(map(lambda word: self.convert_word_to_node(word), words))

        length = nodes[0].length
        stack = [nodes[0]]
        longest = length if nodes[0].is_file else 0

        for i in range(1, len(nodes)):
            node = nodes[i]

            while stack and node.level <= stack[-1].level:
                last_node = stack.pop()
                length = length - 1 - last_node.length

            stack.append(node)
            # "dir" + "/" + "tex.ext"
            length = length + 1 + node.length

            if node.is_file:
                longest = max(longest, length)
        return longest

    def convert_word_to_node(self, word):
        splits = word.split("\t")
        # "\t\ttest" => ['', '', 'test']
        string = splits[-1]
        length = len(string)
        level = len(splits) - 1
        is_file = True if '.' in string else False

        return Node(length, level, is_file)

def main():
    sol = Solution()
    test = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    print(sol.lengthLongestPath(test)) # 32
    print(sol.lengthLongestPath('a.txt')) # 5

if __name__ == '__main__':
    main()

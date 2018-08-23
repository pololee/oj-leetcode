import collections
import string


class Solution:
    ALPHA_LOWERCASE = set(string.ascii_lowercase)

    def find_ladders(self, begin_word, end_word, word_list):
        """
        :type begin_word: str
        :type end_word: str
        :type word_list: [str]
        :rtype list[list[str]]
        """
        word_list = set(word_list)
        if end_word not in word_list:
            return []

        distance_map, neighbors_map = self.bfs_to_set_distance_and_neighbors_map(
            begin_word, end_word, word_list
        )

        paths = []
        self.dfs_to_find_the_shortest_path(
            begin_word, distance_map, neighbors_map, paths, [end_word]
        )
        return paths

    def dfs_to_find_the_shortest_path(self, begin_word, distance_map, neighbors_map, paths, so_far):
        if len(so_far) > 1 and so_far[-1] == begin_word:
            so_far_copy = so_far.copy()
            so_far_copy.reverse()
            paths.append(so_far_copy)
            return

        last_word = so_far[-1]
        for neighbor in neighbors_map[last_word]:
            if distance_map[neighbor] == distance_map[last_word] - 1:
                so_far.append(neighbor)
                self.dfs_to_find_the_shortest_path(
                    begin_word, distance_map, neighbors_map, paths, so_far
                )
                so_far.pop()

    def bfs_to_set_distance_and_neighbors_map(self, begin_word, end_word, word_list):
        distance_map = {}
        distance_map[begin_word] = 0
        neighbors_map = collections.defaultdict(set)
        queue = collections.deque()
        queue.append(begin_word)

        while queue:
            word = queue.popleft()
            if word == end_word:
                break
            for neighbor in self.find_neighbors(word, word_list):
                # This is stunning!!!
                # neighbor is word's neighbor. Insteaf of word -> neighbor
                # we do neighbor -> word
                neighbors_map[neighbor].add(word)
                if neighbor not in distance_map:
                    distance_map[neighbor] = distance_map[word] + 1
                    queue.append(neighbor)

        return distance_map, neighbors_map

    def find_neighbors(self, word, word_list):
        neighbors = set()
        if not word_list:
            return neighbors
        
        if word in word_list:
            word_list.remove(word)

        for i in range(len(word)):
            curr_char = word[i]
            for char in self.ALPHA_LOWERCASE:
                if char == curr_char:
                    continue
                potential_word = word[:i] + char + word[i+1:]
                if potential_word in word_list:
                    neighbors.add(potential_word)

        return neighbors


if __name__ == '__main__':
    sol = Solution()
    begin_word = 'hit'
    end_word = 'cog'
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(sol.find_ladders(begin_word, end_word, word_list))
    begin_word = 'lost'
    end_word = 'miss'
    word_list = ["most", "mist", "miss", "lost", "fist", "fish"]
    print(sol.find_ladders(begin_word, end_word, word_list))

import collections

class Solution:
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    TARGET_STATE = [[1, 2, 3], [4, 5, 0]]

    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        row_size = len(board)
        col_size = len(board[0])

        target_state = self.board_to_string(self.TARGET_STATE)

        start_str = self.board_to_string(board)
        zero_position = self.zero_position(board)

        queue = collections.deque()
        queue.append(
            Node(start_str, 0, self.pos_to_idx(zero_position, col_size))
        )
        visited = set()

        while queue:
            node = queue.popleft()
            cur_board_str = node.board_str
            cur_level = node.level
            cur_idx = node.zero_pos_idx

            if node.board_str == target_state:
                return cur_level

            if cur_board_str in visited:
                continue
            visited.add(node.board_str)

            zero_r, zero_c = self.idx_to_pos(cur_idx, col_size)
            for direction in self.DIRECTIONS:
                new_r = zero_r + direction[0]
                new_c = zero_c + direction[1]

                if new_r >= 0 and new_r < len(board) and new_c >= 0 and new_c < len(board[0]):
                    new_idx = self.pos_to_idx((new_r, new_c), col_size)
                    next_state = self.swap(cur_board_str, cur_idx, new_idx)

                    if next_state not in visited:
                        queue.append(
                            Node(next_state, cur_level + 1, new_idx)
                        )

        return -1

    def pos_to_idx(self, pos, col_size):
        return pos[0] * col_size + pos[1]

    def idx_to_pos(self, idx, col_size):
        return (idx // col_size, idx % col_size)

    def swap(self, board_str, old_idx, new_idx):
        new_str = list(board_str)
        new_str[old_idx] = new_str[new_idx]
        new_str[new_idx] = '0'
        return ''.join(new_str)

    def zero_position(self, board):
        pos = None
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    pos = (i, j)
                    break
        return pos

    def board_to_string(self, board):
        output = ""

        for i in range(len(board)):
            for j in range(len(board[0])):
                output += str(board[i][j])
        return output


class Node:
    def __init__(self, board_str, level, zero_pos_idx):
        self.board_str = board_str
        self.level = level
        self.zero_pos_idx = zero_pos_idx


def main():
    sol = Solution()
    board = [[1, 2, 3], [4, 0, 5]]
    print(sol.slidingPuzzle(board))
    board = [[1, 2, 3], [5, 4, 0]]
    print(sol.slidingPuzzle(board))
    board = [[4, 1, 2], [5, 0, 3]]
    print(sol.slidingPuzzle(board))


if __name__ == '__main__':
    main()

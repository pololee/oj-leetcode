class Solution:
    def solve_n_queens(self, n):
        """
        :type n: int
        :rtype list[list[str]]
        """
        solutions = []
        solution = [-1 for _ in range(n)]
        self.recusive_solve_all(solution, 0, solutions)

        if not solutions:
            return []

        boards = []
        for one_solution in solutions:
            boards.append(self.draw_board(one_solution))

        return boards

    def recusive_solve_all(self, solution, row, solutions):
        if row >= len(solution):
            solutions.append(solution.copy())
            return

        for col_to_try in range(len(solution)):
            if self.is_safe(solution, row, col_to_try):
                self.place_queen(solution, row, col_to_try)
                self.recusive_solve_all(solution, row + 1, solutions)
                self.remove_queen(solution, row)

    def is_safe(self, solution, row, col_to_try):
        for i in range(0, row):
            if solution[i] == col_to_try or abs(i - row) == abs(solution[i] - col_to_try):
                return False
        return True

    def place_queen(self, solution, row, col):
        solution[row] = col

    def remove_queen(self, solution, row):
        solution[row] = -1

    def draw_board(self, solution):
        board = ['.' * len(solution) for _ in range(len(solution))]

        # idx is row, value is col
        for row, col in enumerate(solution):
            new_row = board[row][:col] + 'Q' + board[row][col+1:]
            board[row] = new_row

        return board


if __name__ == '__main__':
    sol = Solution()
    boards = sol.solve_n_queens(4)
    print(boards)

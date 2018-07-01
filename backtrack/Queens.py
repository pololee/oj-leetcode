class Queens:
    def __init__(self, num_of_queens):
        self.size = num_of_queens

    def solve(self, solution, row):
        if row >= self.size:
            return True
        
        for col_to_try in range(self.size):
            if self.is_safe(solution, row, col_to_try):
                self.place_queen(solution, row, col_to_try)
                if self.solve(solution, row + 1):
                    return True
                else:
                    self.remove_queen(solution, row)
        return False

    def solve_all(self, solution, row, solutions):
        if row >= self.size:
            solutions.append(solution.copy()) # you have to make a copy. otherwise remove_queen will reset it back to -1
            return

        for col_to_try in range(self.size):
            if self.is_safe(solution, row, col_to_try):
                self.place_queen(solution, row, col_to_try)
                self.solve_all(solution, row + 1, solutions)
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

if __name__ == '__main__':
    queens = Queens(4)
    answers = []
    solution = [-1 for _ in range(4)]
    queens.solve_all(solution, 0, answers)
    print(answers)  # expected value [[1, 3, 0, 2], [2, 0, 3, 1]]
    # after every try in solve_all, we remove_queen.
    # so solution becomes [-1, -1, -1, -1]
    print(solution)
    queens.solve(solution, 0)
    print(solution)

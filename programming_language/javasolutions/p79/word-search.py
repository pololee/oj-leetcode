class WordSearch:
    def exist(self, board, word):
        if not word:
            return True

        if not board or not board[0]:
            return False

        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)]
                   for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if self.dfs(i, j, 0, word, visited, board):
                    return True
        return False

    def dfs(self, x, y, idx, word, visited, board):
        if idx == len(word):
            return True

        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or visited[x][y] or board[x][y] != word[idx]:
            return False

        visited[x][y] = True
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        answer = False
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if self.dfs(xx, yy, idx + 1, visited, board):
                answer = True
                break

        visited[x][y] = False
        return answer

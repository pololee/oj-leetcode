class DiagonalTraverse:
    def diagonal(self, array):
        m = len(array)
        n = len(array[0])

        # first half
        # first col as starting point
        for k in range(m):
            i = k
            j = 0

            while self.valid(i, j, array):
                print(array[i][j], end=' ')
                i -= 1
                j += 1
            print('')
        
        # second half
        # last row as starting point
        for k in range(1, n):
            i = m - 1
            j = k

            while self.valid(i, j, array):
                print(array[i][j], end=' ')
                i -= 1
                j += 1
            print('')



    def valid(self, i, j, array):
        m = len(array)
        n = len(array[0])

        if i >= 0 and i < m and j >= 0 and j < n:
            return True
        return False

def main():
    test = [['A', 'C', 'F'],
            ['B', 'E', 'H'],
            ['D', 'G', 'I']]
    dig = DiagonalTraverse()
    dig.diagonal(test)

if __name__ == '__main__':
    main()

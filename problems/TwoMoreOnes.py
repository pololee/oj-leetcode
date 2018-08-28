class TwoMoreOnes:
    def has_two_more_ones(self, array):
        if not array or not array[0]:
            return False

        m = len(array)
        n = len(array[0])
        for i in range(m):
            if sum(array[i]) >= 2:
                return True

        for j in range(n):
            col = [array[i][j] for i in range(m)]
            if sum(col) >= 2:
                return True

    def row(self, array):
        m = len(array)
        n = len(array[0])
        for i in range(m):
            if sum(array[i]) >= 2:
                return True
        return False

    def col(self, array):
        m = len(array)
        n = len(array[0])

        for j in range(n):
            col = [array[i][j] for i in range(m)]
            if sum(col) >= 2:
                return True
        return False

    def diagonal(self, array):
        m = len(array)
        n = len(array[0])

        # first half
        # choose each element of the first col as starting point
        # arr[0][0]
        # arr[1][0], arr[0][1]
        # arr[2][0], arr[1][1], arr[0][2]
        # ...
        for k in range(m):
            i = k
            j = 0
            count = 0

            while self.valid_point(i, j, array):
                if array[i][j] == 1:
                    count += 1
                if count >= 2:
                    return True
                i -= 1
                j += 1

        # second half
        # choose each elemnt of the last row as starting point
        for k in range(1, n):
            i = m - 1
            j = k
            count = 0

            while self.valid_point(i, j, array):
                if array[i][j] == 1:
                    count += 1
                if count >= 2:
                    return True
                i -= 1
                j += 1

        return False

    def reverse_diagonal(self, array):
        m = len(array)
        n = len(array[0])

        # first half
        # the first row as starting point
        for k in range(n):
            i = 0
            j = k
            count = 0

            while self.valid_point(i, j, array):
                if array[i][j] == 1:
                    count += 1
                if count >= 2:
                    return True
                i += 1
                j += 1

        # second half
        # the first col as starting point
        for k in range(1, m):
            i = k
            j = 0
            count = 0

            while self.valid_point(i, j, array):
                if array[i][j] == 1:
                    count += 1
                if count >= 2:
                    return True
                i += 1
                j += 1
        return False

    def valid_point(i, j, array):
        m = len(array)
        n = len(array[0])

        if i >= 0 and i < m and j >= 0 and j < n:
            return True
        return False

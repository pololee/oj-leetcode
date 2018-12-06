class Solution:
    def zero_one_full_pack(self, values, sizes, totalCapacity):
        size = len(sizes)

        DP = [[None for _ in range(size + 1)]
              for _ in range(totalCapacity + 1)]

        for i in range(size + 1):
            DP[i][0] = 0

        for i in range(1, size + 1):
            for j in range(1, totalCapacity + 1):
                if sizes[i] > j:
                    DP[i][j] = DP[i-1][j]
                else:
                    a = DP[i-1][j]
                    b = DP[i-1][j-sizes[i]]

                    if not a and not b:
                        DP[i][j] = None
                    elif a is not None and b is not None:
                        DP[i][j] = max(a, b + values[i])
                    elif a is not None:
                        DP[i][j] = a
                    elif b is not None:
                        DP[i][j] = b + values[i]
        return DP[size][totalCapacity]

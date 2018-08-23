class Solution:
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        answer = []
        if not A or not B: return answer
        
        # A is x * y matrix, B is y * z matrix
        # the result is x * z matrix
        x = len(A)
        y = len(A[0])
        z = len(B[0])

        result = [ [0] * z for _ in range(x) ]

        # The point is to avoid doing 0 * 0 operation
        for i in range(x):
            for k in range(y):
                if A[i][k] != 0:
                    for j in range(z):
                        if B[k][j] != 0:
                            result[i][j] += A[i][k] * B[k][j]
        return result

def main():
    sol = Solution()
    A = [[1, 0, 0], [-1, 0, 3]]
    B = [[7, 0, 0], [0, 0, 0], [0, 0 , 1]]
    print(sol.multiply(A, B))

if __name__ == '__main__':
    main()

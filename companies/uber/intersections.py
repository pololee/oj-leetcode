class Intersections:
    def intersections(self, A, B):
        if not A or not B:
            return []
        
        m = len(A)
        n = len(B)
        i = 0
        j = 0

        ans = []
        while i < m and j < n:
            ax, ay = A[i]
            bx, by = B[j]
            interX = max(ax, bx)
            interY = min(ay, by)
            if interX <= interY:
                ans.append([interX, interY])

            if ay < by:
                i += 1
            elif ay > by:
                j += 1
            else:
                i += 1
                j += 1
        
        return ans

def main():
    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1, 5], [8, 12], [15, 18], [20, 24]]
    sol = Intersections()
    print(sol.intersections(A, B))

if __name__ == '__main__':
    main()

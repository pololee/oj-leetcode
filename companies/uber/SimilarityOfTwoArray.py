class Solution:
    def similarity(self, A, B):
        union = set()

        for x in A:
            union.add(x)
        
        numOfSame = 0
        for x in B:
            if x in union:
                numOfSame += 1
            else:
                union.add(x)
        

        return numOfSame / len(union)

def main():
    A = [3, 4, 1, 2, 7]
    B = [6, 1, 3, 5, 10]

    sol = Solution()
    print(sol.similarity(A, B))

if __name__ == '__main__':
    main()

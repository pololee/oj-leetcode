# Given an integer, return all sequences of numbers
# that sum to it.
# E.g. 3 -> (1, 2) (2, 1) (1, 1, 1)

class IntegerDecompose:
    def decompose(self, N):
        """
        :N: int
        :rtype list[list[int]]
        """
        results = []
        self.decompose_util(N, "", N, results)
        return results
    
    def decompose_util(self, remaining, so_far, N, results):
        if remaining < 0:
            return
        
        if remaining == 0:
            results.append(so_far)
            return
        
        for i in range(1, N):
            self.decompose_util(remaining - i, so_far + str(i), N, results)

def main():
    sol = IntegerDecompose()
    print(sol.decompose(3))

if __name__ == '__main__':
    main()

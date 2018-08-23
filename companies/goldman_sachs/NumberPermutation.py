# given N, and [1, 2, 3]
# and return the number of permutations that 
# the sum of the permutation equals to N

# backtracking is not a good way to go.
# Use DP

class NumberPermutation:
    def countPermutations(self, N):
        DP = [0 for _ in range(N + 1)]
        DP[0] = 1
        DP[1] = 1

        for i in range(2, N + 1):
            for num in [1, 2, 3]:
                if i - num >= 0:
                    DP[i] += DP[i-num]
        return DP[N]

def main():
    permute = NumberPermutation()
    print(permute.countPermutations(2))
    print(permute.countPermutations(3))
    print(permute.countPermutations(4))
    print(permute.countPermutations(16))

if __name__ == '__main__':
    main()

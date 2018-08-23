# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution:
    def find_celebrity(self, n):
        if n <= 0: return -1

        # Find the candidate
        # Assume after the following loop, candidate is k
        # That means k doesn't know [k+1..n-1]
        candidate = 0
        for i in range(n):
            if knows(candidate, i): candidate = i
        
        for i range(n):
            if i != candidate and not knows(i, candidate):
                return -1

            if i < candidate and knows(candidate, i):
                return -1
        return candidate

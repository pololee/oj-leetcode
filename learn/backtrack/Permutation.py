# A good variable naming is everything!!!!!!!!!!!!
# so_far vs remaining
# If you have no more characters left to rearrange, print current permutation
# for (every possible choice among the characters left to rearrange) {
#  Make a choice and add that character to the permutation so far
#  Use recursion to rearrange the remaining letters
# }


class Permutation:
    def permute(self, s):
        """
        :s type: str
        :rtype list[str]
        :list all the possible re-arrangements of the letters in a string
        """
        if not s:
            return []

        answer = []
        self.recursive_permute('', s, answer)
        return answer

    def recursive_permute(self, so_far, rest, answer):
        if not rest:
            answer.append(so_far)
            return

        for i in range(len(rest)):
            remaining = rest[0:i] + rest[i+1:]
            self.recursive_permute(so_far + rest[i], remaining, answer)


if __name__ == "__main__":
    per = Permutation()
    print(per.permute('abc'))

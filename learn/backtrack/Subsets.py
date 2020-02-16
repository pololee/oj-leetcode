# If there are no more elements remaining,
# print current subset
# else {
#     Consider the next element of those remaining
#     Try adding it to the current subset, and use recursion to build subsets from here
#     Try not adding it to current subset, and use recursion to build subsets from here
# }


class Subsets:
    def subsets(self, nums):
        """
        :nums list[int]
        :rtype list[list[int]]
        """
        if not nums:
            return []

        answer = []
        self.recursive_subsets([], nums, answer)
        return answer

    def recursive_subsets(self, so_far, rest, answer):
        if not rest:
            answer.append(so_far)
        else:
            add_it = so_far.copy()
            add_it.append(rest[0])
            self.recursive_subsets(add_it, rest[1:], answer)
            self.recursive_subsets(so_far, rest[1:], answer)


if __name__ == '__main__':
    sub = Subsets()
    print(sub.subsets([1, 2, 3]))

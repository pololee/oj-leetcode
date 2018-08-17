class UnionFind:
    def __init__(self, size):
        self.root_ids = [-1 for _ in range(size)]
        self.weights = [0 for _ in range(size)]

    def root(self, x):
        if self.root_ids[x] == -1:
            return -1
        if self.root_ids[x] == x:
            return x

        # path compression
        self.root_ids[x] = self.root_ids[self.root_ids[x]]
        return self.root(self.root_ids[x])

    def find(self, x, y):
        return self.root(x) == self.root(y)

    def union(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)

        if root_x == root_y:
            return

        if self.weights[root_x] < self.weights[root_y]:
            self.root_ids[root_x] = root_y
            self.weights[root_y] += self.weights[root_x]
        else:
            self.root_ids[root_y] = root_x
            self.weights[root_x] += self.weights[root_y]


class Flower:
    def the_day(self, flowers, m, k):
        """
        :type: flowers: list[int]
        :typp m: int
        :type k: int
        :rtype int
        """
        if m * k >= len(flowers):
            return -1

        # according to the stupid setup,
        # flowers[i] = x
        # both i and x are in the range of [1, N]
        # N is the number of positions
        # so the value of pos is 1, ... N
        # so we can have a array of size N + 2
        # then we don't need to worry about 1's left and N's right
        size = len(flowers)
        union_find = UnionFind(size + 2)

        the_final_day = -1  # last day meets the requirements
        num_of_groups = 0  # current number of groups

        for i in range(size):
            day = i + 1
            pos = flowers[i]
            union_find.root_ids[pos] = pos
            union_find.weights[pos] = 1

            # pos's left
            if union_find.root_ids[pos - 1] != -1:
                left_pos_root = union_find.root(pos - 1)
                if union_find.weights[left_pos_root] >= k:
                    num_of_groups -= 1
                union_find.union(pos, left_pos_root)

            # pos's right
            if union_find.root_ids[pos + 1] != -1:
                right_pos_root = union_find.root(pos + 1)
                if union_find.weights[right_pos_root] >= k:
                    num_of_groups -= 1
                union_find.union(pos, right_pos_root)

            if union_find.weights[union_find.root(pos)] >= k:
                num_of_groups += 1

            if num_of_groups == m:
                the_final_day = day

        return the_final_day


def main():
    flower = Flower()
    print(flower.the_day([1, 3, 2], 2, 1))


if __name__ == '__main__':
    main()

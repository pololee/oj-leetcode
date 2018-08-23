class BruteForce:
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """

        size = len(positions)
        heights = [0 for _ in range(size)]
        for i in range(size):
            left, length = positions[i]
            right = left + length
            # This has to be +=
            # because e.g
            # square dropped at position[0] may affect
            # the height when square at position[1] dropped
            # position[0] (0, 3)
            # position[1] (1, 4)
            # when position[0] dropped, heights[0] = 3
            # in the following loop, heights[1] = 3 due to overlap (0, 3)  and (1, 5)
            # when position[1] dropped, heights[1] should be updated to 3 + 4 = 7
            heights[i] += length

            for j in range(i, size):
                # this is to figure how the square drop at position[i]
                # affect all the following dropped squares
                other_left, other_length = positions[j]
                other_right = other_left + other_length
                if other_left < right and other_right > left:
                    heights[j] = max(heights[j], heights[i])

        cur = 0
        answer = []
        for i in range(size):
            cur = max(cur, heights[i])
            answer.append(cur)

        return answer


def main():
    sol = BruteForce()
    print(sol.fallingSquares([[1, 2], [2, 3], [6, 1]]))  # [2, 5, 5]
    print(sol.fallingSquares([[100, 100], [200, 100]]))  # [100, 100]


if __name__ == '__main__':
    main()

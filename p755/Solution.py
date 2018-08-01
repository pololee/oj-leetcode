class Solution:
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        if not heights or not heights[0]:
            return []

        while V > 0:
            filled_idx = K

            for i in reversed(range(K)):
                if heights[i] > heights[filled_idx]:
                    break
                elif heights[i] < heights[filled_idx]:
                    filled_idx = i

            if filled_idx != K:
                heights[filled_idx] += 1
                V -= 1
                continue

            for i in range(K+1, len(heights)):
                if heights[i] > heights[filled_idx]:
                    break
                elif heights[i] < heights[filled_idx]:
                    filled_idx = i

            heights[filled_idx] += 1
            V -= 1

        return heights

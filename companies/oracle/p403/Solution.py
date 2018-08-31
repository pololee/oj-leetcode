class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        table = dict()

        for pos in stones:
            table[pos] = set()

        table[0].add(0)

        for pos in stones:
            for jumpsize in table[pos]:
                for new_jumpsize in range(jumpsize - 1, jumpsize + 2):
                    if new_jumpsize > 0 and pos + new_jumpsize in table:
                        table[pos + new_jumpsize].add(new_jumpsize)

        if len(table[stones[-1]]) > 0:
            return True
        return False

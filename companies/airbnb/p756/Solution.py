import collections


class Solution:
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        allowed_table = collections.defaultdict(set)
        for string in allowed:
            allowed_table[string[0:2]].add(string[-1])

        return self.pyramid_util(bottom, "", allowed_table)

    def pyramid_util(self, current, above, allowed_table):
        if len(current) == 2 and len(above) == 1:
            return True

        if len(current) == len(above) + 1:
            return self.pyramid_util(above, "", allowed_table)

        # above:        m    ?
        # current:    x    y    z
        # the base of ? is current[len(above):len(above) + 2]
        base = current[len(above):len(above) + 2]
        if base in allowed_table:
            for ch in allowed_table[base]:
                if self.pyramid_util(current, above + ch, allowed_table):
                    return True

        return False


def main():
    sol = Solution()
    print(sol.pyramidTransition("XYZ", ["XYD", "YZE", "DEA", "FFF"]))
    print(sol.pyramidTransition("XXYX", ["XXX", "XXY", "XYX", "XYY", "YXZ"]))


if __name__ == '__main__':
    main()

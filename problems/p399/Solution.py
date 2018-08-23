import collections


class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        adj_table = self.graph(equations, values)
        results = []

        for numerator, denom in queries:
            if numerator not in adj_table or denom not in adj_table:
                results.append(-1.0)
                continue

            visited = set()
            visited.add(numerator)
            result = self.dfs_util(adj_table, numerator, 1.0, denom, visited)
            results.append(result)

        return results

    def dfs_util(self, adj_table, string, value_sofar, target, visited):
        if string == target:
            return value_sofar

        for adj_str, adj_value in adj_table[string]:
            if adj_str not in visited:
                visited.add(adj_str)
                result = self.dfs_util(
                    adj_table, adj_str, value_sofar * adj_value, target, visited
                )
                if result != -1.0:
                    return result
                visited.remove(adj_str)

        return -1.0

    def graph(self, equations, values):
        adj_table = collections.defaultdict(list)
        size = len(equations)

        for i in range(size):
            numerator, denom = equations[i]
            value = values[i]

            adj_table[numerator].append((denom, value))
            adj_table[denom].append((numerator, 1.0 / value))

        return adj_table

def main():
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    sol = Solution()
    print(sol.calcEquation(equations, values, queries))

if __name__ == '__main__':
    main()

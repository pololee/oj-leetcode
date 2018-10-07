class Solution:
    """
    @param num: a string contains only digits 0-9
    @param target: An integer
    @return: return all possibilities
    """

    def addOperators(self, num, target):
        # write your code here
        if not num:
            return []

    def dfs(self, num, target, start, path, ans, sumSoFar, lastFactor):
        if start == len(num):
            if sumSoFar == target:
                ans.append(path)

            return

        for i in range(start, len(num)):
            if num[start] == "0" and i > start:
                break

            current = num[start:i+1]
            currentNum = int(current)

            if start == 0:
                self.dfs(num, target, i+1,
                         current, ans,
                         currentNum, currentNum)
            else:
                self.dfs(num, target, i+1,
                         "{}+{}".format(path, current), ans,
                         sumSoFar + current, current)
                self.dfs(num, target, i+1,
                         "{}-{}".format(path, current), ans,
                         sumSoFar-currentNum, -currentNum)
                self.dfs(num, target, i+1,
                         "{}*{}".format(path, current), ans,
                         sumSoFar - lastFactor + lastFactor * currentNum, lastFactor * currentNum)

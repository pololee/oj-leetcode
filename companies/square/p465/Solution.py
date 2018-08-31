import sys


class Solution:
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        if not transactions:
            return 0

        balance = dict()
        for x, y, z in transactions:
            if x not in balance:
                balance[x] = 0
            if y not in balance:
                balance[y] = 0

            balance[x] -= z
            balance[y] += z

        debts = []
        for _, v in balance.items():
            if v == 0:
                continue
            debts.append(v)

        return self.dfs_util(debts, 0)

    # from start in debts, return the min number of transfers needed to 
    # make all debts to be 0
    def dfs_util(self, debts, start):
        result = sys.maxsize

        while start < len(debts) and debts[start] == 0:
            start += 1

        prev = 0
        for i in range(start + 1, len(debts)):
            if debts[i] != prev and debts[i] * debts[start] < 0:
                # transfer debts[start] to debts[i]
                # then we recursively call from start + 1
                # now it assumes debts[start] is 0
                debts[i] += debts[start]
                result = min(result, 1 + self.dfs_util(debts, start + 1))
                debts[i] -= debts[start]
                prev = debts[i]

        # If result == sys.maxsize
        # means it doesn't enter the for loop
        # means all the debts are 0
        # means no more steps needed
        if result == sys.maxsize:
            return 0
        return result
    
    # given debts,
    # before start, `num` transfer needed to make debts before start to be 0
    # return include start, how many transfer needed to make debts to 0
    def dfs_util_2(self, debts, start, num):
        result = sys.maxsize

        while start < len(debts) and debts[start] == 0:
            start += 1
        
        prev = 0
        for i in range(start + 1, len(debts)):
            if debts[i] != prev and debts[i] * debts[start] < 0:
                debts[i] += debts[start]
                result = min(result, self.dfs_util_2(debts, start + 1, num + 1))
                debts[i] -= debts[start]
                prev = debts[i]
        
        # if result == sys.maxsize
        # all debts are 0
        # then the number needed is input `num`
        if result == sys.maxsize:
            return num
        return result

class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []
        
        results = []
        self.dfs_util(results, '', num, 0, target, 0, 0)
        return results
    
    def dfs_util(self, results, path, num, start, target, evaluate, last_value):
        if start == len(num):
            if target == evaluate:
                results.append(path)
            return
        
        for i in range(start, len(num)):
            if num[start] == '0' and i > start:
                break
            
            current = int(num[start:i+1])
            if start == 0:
                self.dfs_util(results, str(current), 
                              num, i + 1,
                              target, current, current)
            else:
                self.dfs_util(results, path + '+' + str(current),
                              num, i + 1,
                              target, evaluate + current, current)
                self.dfs_util(results, path + '-' + str(current),
                              num, i + 1,
                              target, evaluate - current, -current)
                self.dfs_util(results, path + '*' + str(current),
                              num, i + 1,
                              target, evaluate - last_value + last_value * current, last_value * current)


# Why do we need last_value?
# Because when we do “*”, it change the order of evaluation.

# Think about this case
# 2 + 5 * 4
# After + , we have 5, we call it in the else 3 cases,
# The last value is 5. The evaluate is 2 + 5 = 7
# In the next round, when we have * , we need to use 7 - 5 and then have 5 * 4 to get the final evaluation results.

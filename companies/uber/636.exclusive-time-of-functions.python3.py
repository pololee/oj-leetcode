class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        if not logs:
            return []

        ans = [0 for _ in range(n)]
        lastTimeStamp = 0
        stack = []

        for log in logs:
            fid, ftype, ftime = self.parse(log)
            if ftype == "start":
                if stack:
                    ans[stack[-1]] += ftime - lastTimeStamp
                stack.append(fid)
            else:
                ftime += 1
                ans[stack.pop()] += ftime - lastTimeStamp
            lastTimeStamp = ftime
        return ans
    
    def anotherExclusiveTime(self, n, logs):
        if not logs or n > 2 * len(logs):
            return ans
        
        ans = [0 for _ in range(n)]
        fId, _, fTime = self.parse(logs[0])
        stack = [fId]
        prevTime = fTime
        
        for log in logs[1:]:
            fId, fType, fTime = self.parse(log)
            
            if fType == "start":
                if stack:
                    ans[stack[-1]] += (fTime - prevTime)
                stack.append(fId)
                prevTime = fTime
            else:
                ans[stack[-1]] += (fTime - prevTime + 1)
                stack.pop()
                prevTime = fTime + 1
        
        return ans

    def parse(self, log):
        parsed = log.split(":")
        return (int(parsed[0]), parsed[1], int(parsed[2]))

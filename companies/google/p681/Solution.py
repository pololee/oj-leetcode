class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        start = self.str_to_mins(time)
        digits = set()
        for ch in time:
            if ch == ':':
                continue
            digits.add(int(ch))
        
        if len(digits) == 1:
            return time

        answer = start
        elapsed = 24 * 60
        for h1 in digits:
            for h2 in digits:
                if h1 * 10 + h2 >= 24:
                    continue
                for m1 in digits:
                    for m2 in digits:
                        if m1 * 10 + m2 >= 60:
                            continue
                        
                        current = 60 * (h1 * 10 + h2) + (m1 * 10 + m2)
                        cur_elapsed = (current - start) % (24 * 60)
                        if cur_elapsed > 0 and cur_elapsed < elapsed:
                            answer = current
                            elapsed = cur_elapsed
        return self.mins_to_str(answer)

    def str_to_mins(self, time):
        # 01:34
        hour = int(time[0:2])
        minute = int(time[3:])

        return hour * 60 + minute
    
    def mins_to_str(self, mins):
        hour = mins // 60
        minute = mins % 60

        return "{:02d}:{:02d}".format(hour, minute)

def main():
    sol = Solution()
    print(sol.nextClosestTime('00:01'))
    print(sol.nextClosestTime('00:00'))
    print(sol.nextClosestTime('19:34'))
    print(sol.nextClosestTime('23:59'))
    print(sol.nextClosestTime('20:48'))

if __name__ == '__main__':
    main()

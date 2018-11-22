# process_loan(loan_amount)
# get_loan_volume()

# process_loan(10) min 1
# process_loan(10) min 59
# get_loan_volume() -> 20  min 60
# get_loan_volume() -> 0 min 120

from datetime import *
import time
from collections import deque


class Solution:
    DELTA = timedelta(seconds=2)

    def __init__(self):
        self.queue = deque()
        self.accuSum = 0

    def process_loan_volumn(self, load_amount):
        time = datetime.now()
        self.queue.append((time, load_amount))
        self.accuSum += load_amount

    def get_load_volumn(self):
        curr = datetime.now()

        while self.queue:
            qTime, qAmt = self.queue[0]
            if qTime + self.DELTA < curr:
                self.queue.popleft()
                self.accuSum -= qAmt
            else:
                break
        return self.accuSum


class ConstantSolution:
    DELTA = timedelta(seconds=2)

    def __init__(self):
        self.array = []

    def process_loan_volumn(self, load_amount):
        curr = datetime.now()
        if not self.array:
            self.array.append((curr, load_amount))
        else:
            t, amt = self.array[-1]
            if t + self.DELTA > curr:
                self.array[-1] = (t, amt + load_amount)
            else:
                self.array.append(curr, load_amount)

    def get_load_volumn(self):
        return self.array[-1][1]


if __name__ == "__main__":
    sol = Solution()
    sol.process_loan_volumn(10)
    time.sleep(3)
    sol.process_loan_volumn(10)
    print(sol.get_load_volumn())

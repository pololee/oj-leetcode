import unittest
from IPython import embed

class GuessServer:
    def __init__(self, target):
        self.target = target
        self.callCount = 0

    def guess(self, tryNumber):
        self.callCount += 1
        cnt = 0
        for i in range(len(self.target)):
            if tryNumber[i] == self.target[i]:
                cnt += 1

        return cnt


class GuessNumberI:
    def findTheNumber(self, guessServer):
        table = {
            '1111': 0,
            '2222': 0,
            '3333': 0,
            '4444': 0,
            '5555': 0
        }

        for num in table:
            cnt = guessServer.guess(num)
            if cnt == 4:
                return num
            table[num] = cnt
        table['6666'] = 4 - sum(table.values())

        # this give us what numbers the target has
        # and the frequency of each number
        counter = dict()
        for key, value in table.items():
            if value == 0:
                continue
            counter[key[0]] = value

        permutation = PermutationII()

        return permutation.find([], counter, guessServer)

class PermutationII:
    def find(self, sofar, table, guessServer):
        if len(sofar) == 4:
            number = ''.join(sofar)
            if guessServer.guess(number) == 4:
                return number
            return ''
        else:
            for num, freq in table.items():
                if freq > 0:
                    table[num] -= 1
                    sofar.append(num)
                    answer = self.find(sofar, table, guessServer)
                    if answer and len(answer) == 4:
                        return answer
                    table[num] += 1
                    sofar.pop()

class SolutionTest(unittest.TestCase):
    sol = GuessNumberI()
    guessServer = GuessServer('4321')

    def testFind(self):
        self.assertEqual('4321', self.sol.findTheNumber(self.guessServer))
        print(self.guessServer.callCount)

if __name__=='__main__':
    unittest.main()

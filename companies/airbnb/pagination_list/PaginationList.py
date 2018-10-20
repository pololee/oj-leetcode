import unittest


class Solution:
    def reorderListings(self, inputCsvArray, pageSize):
        if not inputCsvArray:
            return []

        size = len(inputCsvArray)
        lineIdSet = set()
        for i in range(size):
            lineIdSet.add(i)

        ans = []
        pageHostId = set()
        counter = 0
        idx = 0
        while lineIdSet:
            if idx not in lineIdSet:
                idx += 1
                continue
            hostId = self.getHostId(inputCsvArray, idx)

            if hostId not in pageHostId:
                pageHostId.add(hostId)
                ans.append(inputCsvArray[idx])
                counter += 1
                lineIdSet.remove(idx)
                idx += 1
            else:
                nextDiffHostLindIdx = self.findNextDiffHost(
                    idx, inputCsvArray, lineIdSet
                )
                if nextDiffHostLindIdx == -1:
                    pageHostId.add(hostId)
                    ans.append(inputCsvArray[idx])
                    counter += 1
                    lineIdSet.remove(idx)
                    idx += 1
                else:
                    line = inputCsvArray[nextDiffHostLindIdx]
                    pageHostId.add(self.getHostId(
                        inputCsvArray, nextDiffHostLindIdx))
                    ans.append(line)
                    counter += 1
                    lineIdSet.remove(nextDiffHostLindIdx)
                    idx = nextDiffHostLindIdx + 1

            if counter == pageSize:
                pageHostId = set()
                counter = 0
                ans.append('')
                if lineIdSet:
                    idx = min(lineIdSet)
            
            if lineIdSet and idx >= size:
                idx = min(lineIdSet)
        return ans

    def findNextDiffHost(self, lineIdx, inputCsvArray, lineIdSet):
        targetHostId = self.getHostId(inputCsvArray, lineIdx)
        size = len(inputCsvArray)

        for idx in range(lineIdx+1, size):
            if idx not in lineIdSet:
                continue
            currHostId = self.getHostId(inputCsvArray, idx)
            if currHostId != targetHostId:
                return idx
        return -1

    def getHostId(self, inputCsvArray, idx):
        if idx >= len(inputCsvArray):
            raise Exception('idx out of range')
        curr = inputCsvArray[idx]
        return curr.split(',')[0]
    
    def firstNotVisited(self, visited):
        for i in range(len(visited)):
            if not visited[i]:
                return i
        return len(visited)


class SolutionTest(unittest.TestCase):
    sol = Solution()

    def test1(self):
        input = [
            "1,28,300.1,SanFrancisco",
            "4,5,209.1,SanFrancisco",
            "20,7,208.1,SanFrancisco",
            "23,8,207.1,SanFrancisco",
            "16,10,206.1,Oakland",
            "1,16,205.1,SanFrancisco",
            "6,29,204.1,SanFrancisco",
            "7,20,203.1,SanFrancisco",
            "8,21,202.1,SanFrancisco",
            "2,18,201.1,SanFrancisco",
            "2,30,200.1,SanFrancisco",
            "15,27,109.1,Oakland",
            "10,13,108.1,Oakland",
            "11,26,107.1,Oakland",
            "12,9,106.1,Oakland",
            "13,1,105.1,Oakland",
            "22,17,104.1,Oakland",
            "1,2,103.1,Oakland",
            "28,24,102.1,Oakland",
            "18,14,11.1,SanJose",
            "6,25,10.1,Oakland",
            "19,15,9.1,SanJose",
            "3,19,8.1,SanJose",
            "3,11,7.1,Oakland",
            "27,12,6.1,Oakland",
            "1,3,5.1,Oakland",
            "25,4,4.1,SanJose",
            "5,6,3.1,SanJose",
            "29,22,2.1,SanJose",
            "30,23,1.1,SanJose"
        ]
        ans = self.sol.reorderListings(input, 12)
        self.assertEqual(32, len(ans))
        print('\n'.join(ans))
        self.assertEqual("1,28,300.1,SanFrancisco", ans[0])
        self.assertEqual("11,26,107.1,Oakland", ans[11])
        self.assertEqual("", ans[12])


if __name__ == '__main__':
    unittest.main()

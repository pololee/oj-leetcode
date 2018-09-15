import collections


class TagList:
    def minimumWindow(self, targetList, availableTagList):
        # assume no duplicates in targetList
        if not targetList or not availableTagList:
            return [0]
        if len(targetList) > len(availableTagList):
            return [0]

        # assume no duplicates in targetList
        targetSet = set(targetList)
        availableTable = dict()

        targetSize = len(targetList)
        availableSize = len(availableTagList)

        start = availableSize
        minLength = availableSize + 1
        j = 0
        matchedTags = 0

        for i in range(availableSize):
            while j < availableSize and matchedTags < targetSize:
                tag = availableTagList[j]

                if tag not in availableTable:
                    availableTable[tag] = 1
                else:
                    availableTable[tag] += 1

                if tag in targetSet and availableTable[tag] == 1:
                    matchedTags += 1
                j += 1

            if matchedTags == targetSize:
                if j - i < minLength:
                    start = i
                    minLength = j - i

            tag = availableTagList[i]
            if tag in targetSet:
                if availableTable[tag] == 1:
                    matchedTags -= 1
                availableTable[tag] -= 1

        if start < availableSize:
            return [start, start + minLength - 1]
        return [0]


def main():
    sol = TagList()
    targetList = ['a0', 'b1']
    availableTagList = ['b1', 'x3', 'b1', 'a0', 'b1']
    print(sol.minimumWindow(targetList, availableTagList))


if __name__ == '__main__':
    main()

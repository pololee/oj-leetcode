import collections


class TreeNode:
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq
        self.left = None
        self.right = None


class ScoreGathering:
    def scoreGather(self, stream):
        if not stream:
            return ""

        root = None
        for target in stream:
            root = self.insert(root, target)

        return self.serializeTree(root)

    def insert(self, root, target):
        if root is None:
            return TreeNode(target, 1)

        if target > root.val:
            root.right = self.insert(root.right, target)
        elif target < root.val:
            root.left = self.insert(root.left, target)
        else:
            root.freq += 1

        return root

    def serializeTree(self, root):
        if not root:
            return ""

        strList = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node is None:
                strList.append('')
            else:
                strList.append("{}:{}".format(node.val, node.freq))
                if node.left or node.right:
                    queue.append(node.left)
                    queue.append(node.right)

        return ','.join(strList)


def main():
    gather = ScoreGathering()
    test = [4, 2, 5, 5, 6, 1, 4]
    print(gather.scoreGather(test))


if __name__ == '__main__':
    main()

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BstDistance:
    def bstDistance(self, values, node1, node2):
        """
        :values type: list[int]
        :node1 type: int
        :node2 type: int
        :rtype int
        """
        if not values:
            return -1

        root = self.buildBst(values)
        dist1 = self.rootPathLength(root, node1)
        dist2 = self.rootPathLength(root, node2)

        if dist1 == -1 or dist2 == -1:
            return -1

        lca = self.lowestCommonAncestor(root, node1, node2)
        lcaDist = self.rootPathLength(root, lca.val)

        return dist1 + dist2 - 2 * lcaDist

    def buildBst(self, values):
        root = None

        for value in values:
            root = self.insert(root, value)

        return root

    def insert(self, root, target):
        if root is None:
            return TreeNode(target)

        if target < root.val:
            root.left = self.insert(root.left, target)
        elif target > root.val:
            root.right = self.insert(root.right, target)

        return root

    def rootPathLength(self, root, target):
        if root is None:
            return -1

        if target == root.val:
            return 0
        elif target < root.val:
            dist = self.rootPathLength(root.left, target)
            if dist != -1:
                return 1 + dist
        else:
            dist = self.rootPathLength(root.right, target)
            if dist != -1:
                return 1 + dist

        return -1

    # distance = rootDistance(A) + rootDistance(B) - rootDistance(LCA) lowest common ancestor

    def lowestCommonAncestor(self, root, target1, target2):
        if root is None or root.val == target1 or root.val == target2:
            return root

        if target1 < root.val and target2 < root.val:
            return self.lowestCommonAncestor(root.left, target1, target2)
        elif target1 > root.val and target2 > root.val:
            return self.lowestCommonAncestor(root.right, target1, target2)

        return root


def main():
    sol = BstDistance()
    values = [5, 6, 3, 1, 2, 4]
    root = sol.buildBst(values)
    # print(sol.rootPathLength(root, 5))
    # print(sol.rootPathLength(root, 4))
    # print(sol.rootPathLength(root, 2))
    # print(sol.rootPathLength(root, 1000))  # -1

    print(sol.bstDistance(values, 4, 5))


if __name__ == '__main__':
    main()

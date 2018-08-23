class Solution:
    def find_target(self, root, k):
        """
        :root: TreeNode
        :k: int
        :rtype bool
        """
        sorted_array = []
        self.first_order_traverse(root, sorted_array)

        i = 0
        j = len(sorted_array) - 1
        while i < j:
            current_sum = sorted_array[i] + sorted_array[j]

            if current_sum == k:
                return True
            elif current_sum > k:
                j -= 1
            else:
                i += 1
        return False
    
    def first_order_traverse(self, root, array):
        if root.left:
            self.first_order_traverse(root.left, array)
        
        array.append(root.val)

        if root.right:
            self.first_order_traverse(root.right, array)
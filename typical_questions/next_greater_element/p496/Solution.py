class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1:
            return []
        
        table = dict()
        stack = [nums2[0]]
        for i in range(1, len(nums2)):
            num = nums2[i]

            while stack and stack[-1] < num:
                small = stack.pop()
                table[small] = num
            
            stack.append(num)
        
        while stack:
            num = stack.pop()
            table[num] = -1
        
        results = list(map(lambda x: table[x], nums1))

        return results

def main():
    sol = Solution()
    print(sol.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))  # [-1,3,-1]
    print(sol.nextGreaterElement([2, 4], [1, 2, 3, 4])) # [3, -1]

if __name__ == '__main__':
    main()

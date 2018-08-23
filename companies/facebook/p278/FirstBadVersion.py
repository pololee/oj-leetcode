class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n

        while low < high:
            middle = low + (high - low) // 2

            if self.isBadVersion(middle):
                high = middle
            else:
                low = middle + 1
        
        return high


    def isBadVersion(self, version):
        if version >= 2:
            return True

        return False

class Solution:
    def my_sqrt(self, x):
        """
        :typr x: int
        :rtype int
        """
        if x <= 1:
            return x
        
        low = 1
        high = x
        answer = 0

        while low <= high:
            mid = low + (high - low) // 2
            tmp = x // mid

            if mid == tmp:
                return mid
            elif mid < tmp:
                answer = mid
                low = mid + 1
            else:
                high = mid - 1
        return answer

if __name__ == '__main__':
    sol = Solution()
    print(sol.my_sqrt(8))
    print(sol.my_sqrt(4))
    print(sol.my_sqrt(2))
    print(sol.my_sqrt(1))
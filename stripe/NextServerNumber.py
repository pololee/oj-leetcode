class NextServerNumber:
    def nextNumber(self, nums):
        if not nums:
            return 1
        nums_set = set()

        for n in nums:
            nums_set.add(n)
        
        max_num = max(nums_set)
        for i in range(1, max_num + 1):
            if i not in nums_set:
                return i
        
        return max_num + 1

def main():
    sol = NextServerNumber()
    print(sol.nextNumber([])) #1
    print(sol.nextNumber([1, 2, 5])) # 3
    print(sol.nextNumber([2, 3]))

if __name__ == '__main__':
    main()

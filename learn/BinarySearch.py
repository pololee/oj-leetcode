class BinarySearch:
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1
        middle = 0

        while low <= high:
            middle = low + (high - low) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                low = middle + 1
            else:
                high = middle - 1

        return -1

    def lower_bound_search(self, nums, target):
        """
        Given an sorted array, find the first element
        that is greater than or equal to the target
        """
        low = 0
        high = len(nums) - 1
        middle = 0

        while low <= high:
            middle = low + (high - low) // 2

            if nums[middle] >= target and (middle == 0 or nums[middle-1] < target):
                return middle
            elif nums[middle] >= target:
                high = middle - 1
            else:
                low = middle + 1

        return -1

    def upper_bound_search(self, nums, target):
        """
        Given an sorted array, find the first element
        that is greater than the target
        """
        low = 0
        high = len(nums) - 1
        middle = 0

        while low <= high:
            middle = low + (high - low) // 2

            if nums[middle] > target and (middle == 0 or nums[middle-1] <= target):
                return middle
            elif nums[middle] > target:
                high = middle - 1
            else:
                low = middle + 1
        
        return -1

def main():
    search = BinarySearch()

    nums_1 = [0, 5, 13, 19, 22, 41, 55, 68, 72, 81, 98]
    print(search.search(nums=nums_1, target=55)) # answer is 6
    print(search.search(nums=nums_1, target=100)) # answer is -1 (not found)

    nums_2 = [1, 1, 2, 4, 5, 5, 5, 6, 6, 6, 6, 8, 10, 10, 11]
    print_str = 'index: {}, value: {}'
    low_bound_index = search.lower_bound_search(nums=nums_2, target=6) # answer is 7
    print(print_str.format(low_bound_index, nums_2[low_bound_index]))
    uppper_bound_index = search.upper_bound_search(nums=nums_2, target=6) # answer is 11
    print(print_str.format(uppper_bound_index, nums_2[uppper_bound_index]))

    print(search.lower_bound_search(nums=nums_2, target=0)) # answer is 0, the first element
    print(search.lower_bound_search(nums=nums_2, target=12)) # answer is -1, not found
    print(search.upper_bound_search(nums=nums_2, target=12)) # answer is -1, not found

if __name__ == '__main__':
    main()
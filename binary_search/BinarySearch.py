class BinarySearch:
    def find_target(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # now left == right
        if nums[left] == target:
            return left
        return -1

    def upper_bound(self, nums, target):
        """
        Return the first element that is greater than target
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            # because we have (right - left) // 2
            # so when right = left + 1
            # mid = left
            # in the following change, we have left = mid + 1 or right = mid
            # then in this round, left will be equal to right
            mid = left + (right - left) // 2

            if nums[mid] <= target:
                # because I'm looking for greater than, so less or/and equal
                # I 'll drop mid value
                left = mid + 1
            else:
                # because I'm lookfing for greater that, so larger
                # I'll include the mid value, it cound be the final value
                right = mid
        if nums[right] > target:
            return right
        return -1

    def lower_bound(self, nums, target):
        """
        return the first element that is smaller that target
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            # when there are two element left,
            # the if else will run, left = mid or right = mid - 1
            # if I use mid = (left + right) // 2
            # the if nums[mid] < target, left = mid
            # it will get into endless loop,
            # we need to advance mid to avoid endless loop
            # Note that in the above binary search we choose the upper middle element
            # (left + right + 1)// 2 instead of the lower element (left + right) // 2
            #  The reason is due to the terminating condition when there are two elements left.
            # If we chose the lower middle element and the condition nums[mid] < target evaluates to true
            # then the loop will never terminate. Choosing the upper middle element will guarantee termination.
            mid = (left + right + 1) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid - 1

        if nums[left] < target:
            return left
        return -1


def main():
    binary = BinarySearch()
    test = [1, 2, 3]
    print("Find target:")
    print(binary.find_target(test, 0))
    print(binary.find_target(test, 1))
    print(binary.find_target(test, 2))
    print(binary.find_target(test, 3))
    print(binary.find_target(test, 4))

    print("upper bound: the first element that is greater than target")
    print(binary.upper_bound(test, 0))
    print(binary.upper_bound(test, 1))
    print(binary.upper_bound(test, 2))
    print(binary.upper_bound(test, 3))
    print(binary.upper_bound(test, 4))

    print("lower bound: the first element that is smaller than target")
    print(binary.lower_bound(test, 0))
    print(binary.lower_bound(test, 1))
    print(binary.lower_bound(test, 2))
    print(binary.lower_bound(test, 3))
    print(binary.lower_bound(test, 4))


if __name__ == '__main__':
    main()

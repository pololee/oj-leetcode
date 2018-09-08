import unittest


class SortWithReverse:
    def reverse(self, nums, end):
        left, right = 0, end
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def sort(self, nums):
        for i in reversed(range(len(nums))):
            maxNum = max(nums[:i+1])
            idx = nums.index(maxNum)
            self.reverse(nums, idx)
            self.reverse(nums, i)

class ReverseBoolean:
    def reverse(self, array, end):
        for i in range(end + 1):
            array[i] = not array[i]
        
        left, right = 0, end
        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    
    def all_to_true(self, array):
        for i in reversed(range(len(array))):
            if array[0]:
                array[0] = False
            self.reverse(array, i)


class SortWithReverseTest(unittest.TestCase):
    def test_reverse(self):
        sorter = SortWithReverse()
        nums = [5, 6, 3, 2]
        sorter.reverse(nums, 2)
        self.assertEqual([3, 6, 5, 2], nums)
    
    def test_sort(self):
        sorter = SortWithReverse()
        nums = [5, 6, 3, 2]
        sorter.sort(nums)
        self.assertEqual([2, 3, 5, 6], nums)

class ReverseBooleanTest(unittest.TestCase):
    def test_all_to_true(self):
        array = [True, False, False, False, True, True]
        reverse = ReverseBoolean()
        reverse.all_to_true(array)
        self.assertTrue(all(array))



def main():
    unittest.main()


if __name__ == '__main__':
    main()

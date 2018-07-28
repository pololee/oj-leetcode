import collections


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []

        queue = collections.deque()
        for i in range(k-1):
            self.in_queue(queue, nums[i])

        answer = []
        for i in range(k-1, len(nums)):
            self.in_queue(queue, nums[i])
            answer.append(queue[0])
            self.de_queue(queue, nums[i - k + 1])

        return answer

    def in_queue(self, queue, num):
        while queue and queue[-1] < num:
            queue.pop()

        queue.append(num)

    def de_queue(self, queue, num):
        if queue and queue[0] == num:
            queue.popleft()

def main():
    sol = Solution()
    print(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))

if __name__ == '__main__':
    main()

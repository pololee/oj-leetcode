from collections import Counter

class Solution:
    def least_interval(self, tasks, n):
        counter_of_each_task = Counter(tasks)
        counters = list(counter_of_each_task.values())
        sorted_counters = sorted(counters)

        max_counter = sorted_counters[-1]
        num_of_task_with_max_counter = sorted_counters.count(max_counter)

        chunk_len = n + 1
        number_of_chunks = max_counter - 1

        # why we need max?
        # example: 3A 2B 2C n = 1,
        # it will be 
        # A?A?A -> ABABA -> ABCABCA
        # Because the interval is too small. By just having the tasks without any idles,
        # it's enough to have same tasks separated with enough distance by the actual task, not idles
        # so the results end up with the length of the tasks
        return max(len(tasks), chunk_len * number_of_chunks + num_of_task_with_max_counter)


def main():
    sol = Solution()
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print(sol.least_interval(tasks, n))

if __name__ == '__main__':
    main()
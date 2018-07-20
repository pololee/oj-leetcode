import collections

class SolutionII:
    def least_interval(self, tasks, n):
        counter_of_each_task = collections.Counter(tasks)
        counters = list(counter_of_each_task.values())

        max_counter = max(counters)
        num_of_tasks_with_max_counter = counters.count(max_counter)

        num_of_interval_divided_max = max_counter - 1
        # assume task A has the max_counter
        # task B has the same count as A
        # the minimum length between those intervals is n
        # B has to be placed next to A
        # num_of_tasks_with_max_counter is 2
        # the actual interval becomes n - (2 - 1)
        # - 1 is to take off A from the num_of_tasks_with_max_counter
        interval_length = n - (num_of_tasks_with_max_counter - 1)
        empty_slots = num_of_interval_divided_max * interval_length
        available_tasks = len(tasks) - num_of_tasks_with_max_counter * max_counter
        idles = max(0, empty_slots - available_tasks)

        return len(tasks) + idles


def main():
    sol = SolutionII()
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print(sol.least_interval(tasks, n))

if __name__ == '__main__':
    main()


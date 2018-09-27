import heapq


class TopKSellingFood:
    def top_k_selling_food(self, sales, k):
        sales_counter = [dict() for _ in range(24)]

        for _, food, hour in sales:
            sales_counter[hour][food] = sales_counter[hour].get(food, 0) + 1
        
        ans = [list() for _ in range(24)]
        for idx, counter in enumerate(sales_counter):
            top_k = ans[idx]
            for food, count in counter.items():
                if len(top_k) < k:
                    heapq.heappush(top_k, (count, food))
                else:
                    tmp_count, tmp_food = top_k[0]
                    if count > tmp_count:
                        heapq.heappop(top_k)
                        heapq.heappush(top_k, (count, food))
        return list(map(lambda array: [item[1] for item in array], ans))


def main():
    sol = TopKSellingFood()
    sales = [(0, 'apple', 0),
             (1, 'apple', 0),
             (2, 'orange', 1),
             (3, 'orange', 0)]
    print(sol.top_k_selling_food(sales, 1))


if __name__ == '__main__':
    main()

from decimal import Decimal


class Solution:
    ZERO = Decimal('0.0')

    def possible_orders(self, menu, targetAmt):
        if not menu:
            return []

        targetAmt = Decimal(str(targetAmt))
        menu = self.decimalify_price(menu)
        orders = []
        curr_order = dict()
        self.backtrack(curr_order, orders, menu, targetAmt)
        return orders

    def decimalify_price(self, menu):
        table = dict()

        for food, price in menu.items():
            table[food] = Decimal(str(price))

        return table

    def same_order(self, curr_order, orders):
        for order in orders:
            to_match = len(order)

            for food, cnt in order.items():
                if food not in curr_order:
                    return False

                if curr_order[food] == cnt:
                    to_match -= 1

                if to_match == 0:
                    return True
        return False

    def backtrack(self, curr_order, orders, menu, targetAmt):
        if targetAmt < self.ZERO:
            return

        if targetAmt == self.ZERO:
            if not self.same_order(curr_order, orders):
                orders.append(curr_order.copy())
                return

        for food, price in menu.items():
            if price > targetAmt:
                continue

            if food in curr_order:
                curr_order[food] += 1
            else:
                curr_order[food] = 1
            targetAmt -= price
            self.backtrack(curr_order, orders, menu, targetAmt)
            if curr_order[food] == 1:
                del curr_order[food]
            else:
                curr_order[food] -= 1
            targetAmt += price


if __name__ == "__main__":
    sol = Solution()
    menu = {
        "fruit": 2.15,
        "fris": 2.75,
        "salad": 3.35,
        "wings": 3.55,
        "sticks": 4.20,
        "plate": 5.80
    }
    targetAmt = 15.05
    sol = Solution()
    ans = sol.possible_orders(menu, targetAmt)
    print([dict(x) for x in ans])

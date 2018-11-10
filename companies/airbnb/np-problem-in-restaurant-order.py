# https://xkcd.com/287/

from decimal import *
from collections import *
import unittest


class Solution:
    def possibleOrders(self, menu, targetAmt):
        if not menu:
            return []
        targetAmt = Decimal(str(targetAmt))
        if targetAmt <= Decimal("0.0"):
            return []
        menu = self.decimalifyMenu(menu)
        ans = []
        self.backtrackUtil([], ans, menu, targetAmt)
        return ans

    def decimalifyMenu(self, menu):
        table = dict()
        for key, value in menu.items():
            table[key] = Decimal(str(value))

        return table

    def backtrackUtil(self, items, ans, menu, amt):
        if amt == Decimal("0.0"):
            if not self.sameOrderExist(items, ans):
                ans.append(list(items))
            return

        if amt < Decimal("0.0"):
            return

        for item in menu:
            if menu[item] > amt:
                continue

            items.append(item)
            amt -= menu[item]
            self.backtrackUtil(items, ans, menu, amt)
            items.pop()
            amt += menu[item]

    def sameOrderExist(self, items, ans):
        table = Counter(items)

        for order in ans:
            xTable = Counter(order)
            matched = len(table)

            for key in table:
                if key in xTable and table[key] == xTable[key]:
                    matched -= 1
                else:
                    break
            if matched == 0:
                return True
        return False


class SolutionTest(unittest.TestCase):
    def testSameOrderExist(self):
        items = ["b", "a"]
        ans = [["a", "b"]]
        sol = Solution()
        self.assertTrue(sol.sameOrderExist(items, ans))

    def testPossibleOrders__none_menu(self):
        sol = Solution()
        self.assertEqual([], sol.possibleOrders(dict(), 1.2))

    def testPossibleOrders__negative_target_amt(self):
        sol = Solution()
        self.assertEqual([], sol.possibleOrders({"a": 1.3}, -1.2))

    def testPossibleOrders(self):
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
        ans = sol.possibleOrders(menu, targetAmt)
        self.assertEqual(2, len(ans))
        self.assertCountEqual(
            ['fruit', 'fruit', 'fruit', 'fruit', 'fruit', 'fruit', 'fruit'],
            ans[0]
        )
        self.assertCountEqual(['fruit', 'wings', 'wings', 'plate'], ans[1])



unittest.main()

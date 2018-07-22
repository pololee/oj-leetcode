class GenericSolution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        T_i10 = 0
        T_i11 = None
        # T[i][1][0] = max(T[i-1][1][0], T[i-1][1][1] + prices[i])
        # T[i][1][1] = max(T[i-1][1][1], T[i-1][0][0] - prices[i])
        #            = max(T[i-1][1][1], -prices[i])
        # T[i-1][0][0] is awalys equal to 0
        # T[-1][1][0] = 0
        # T[-1][1][1] = negative infinity
        for price in prices:
            if T_i11:
                T_i10 = max(T_i10, T_i11 + price)
            if T_i11:
                T_i11 = max(T_i11, 0 - price)
            else:
                T_i11 = (0 - price)
        return T_i10


def main():
    gsol = GenericSolution()
    print(gsol.maxProfit([7, 1, 5, 3, 6, 4]))


if __name__ == '__main__':
    main()

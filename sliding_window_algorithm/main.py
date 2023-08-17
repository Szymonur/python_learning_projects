def main():
    l, r = 0, 1  # r = buy, r= sell
    max_p = 0
    prices = [9, 1, 7, 3, 0, 5]

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_p = max(max_p, profit)
        else:
            l = r
        r += 1
    return max_p


if __name__ == '__main__':
    print(main())

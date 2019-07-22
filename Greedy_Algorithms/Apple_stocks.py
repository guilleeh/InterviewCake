'''
Writing programming interview questions hasn't made me rich yet ... so I might give up and start trading Apple stocks all day instead.

First, I wanna know how much money I could have made yesterday if I'd been trading Apple stocks all day.

So I grabbed Apple's stock prices from yesterday and put them in a list called stock_prices, where:

The indices are the time (in minutes) past trade opening time, which was 9:30am local time.
The values are the price (in US dollars) of one share of Apple stock at that time.
So if the stock cost $500 at 10:30am, that means stock_prices[60] = 500.

Write an efficient function that takes stock_prices and returns the best profit I could have made from one purchase and one sale of one share of Apple stock yesterday.

For example:

  stock_prices = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices)
# Returns 6 (buying for $5 and selling for $11)

No "shorting"—you need to buy before you can sell. Also, you can't buy and sell in the same time step—at least 1 minute has to pass.
'''

import sys


def get_max_profit(stocks: list) -> int:
    max_profit = -sys.maxsize
    if len(stocks) == 1:
        return max_profit

    current_stock = stocks[0]

    for stock in stocks[1:]:
        if stock < current_stock:
            current_stock = stock
        else:
            print(max_profit, stock - current_stock)
            if stock - current_stock > max_profit:
                max_profit = stock - current_stock

    return max_profit


test_1 = [10, 7, 5, 8, 11, 9]
test_2 = [1, 1, 1, 1, 1, 1]
test_3 = [1, 5, 3, 2]
test_4 = [7, 2, 8, 9]
test_5 = [1, 6, 7, 9]

print(get_max_profit(test_1) == 6)
print(get_max_profit(test_2) == 0)
print(get_max_profit(test_3) == 4)
print(get_max_profit(test_4) == 7)
print(get_max_profit(test_5) == 8)

'''
Time Complexity: O(N)
Space Complexity: O(1)
'''

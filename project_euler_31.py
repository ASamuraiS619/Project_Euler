# -*- coding: utf-8 -*-

'''
Problem31 「Coin sums」

In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
(合計が£2になる硬貨の枚数の組み合わせは全部で何通り？)
'''

import time

def count_combinations(target, coins):
    if len(coins) == 1 and target % coins[0] == 0:
        return 1
    elif len(coins) == 1 and target % coins[0] != 0:
        return None
    count = 0
    for i in range(target // coins[0] + 1):
        count += count_combinations(target - coins[0] * i, coins[1:])
    return count

if __name__ == '__main__':
    start = time.time()

    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    target = 200

    answer = count_combinations(target, coins)

    print(answer)   # answer 73682

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.03221sec

# -*- coding: utf-8 -*-

'''
Problem56 「Powerful digit sum」

A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
(a, b < 100のとき、a^bの全桁の合計の最大値を求めよ。)
'''

import time

if __name__ == '__main__':
    start = time.time()

    maximum = 0
    for a in range(1, 100):
        for b in range(1, 100):
            _sum = sum(map(int, str(a ** b)))
            if _sum > maximum:
                maximum = _sum

    print(maximum)  # answer 972

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.1033sec


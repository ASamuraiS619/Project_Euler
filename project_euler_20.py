# -*- coding: utf-8 -*-

'''
Problem20 「各位の数字の和 2」

n × (n - 1) × ... × 3 × 2 × 1 を n! と表す.
例えば, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800 となる.
この数の各桁の合計は 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27 である.
では, 100! の各位の数字の和を求めよ.

注: Problem 16 も各位の数字の和に関する問題です。解いていない方は解いてみてください。
'''

import time
from functools import reduce

if __name__ == '__main__':
    start = time.time()

    numbers = list(range(1, 101))
    # 100!を計算
    target = reduce(lambda x, y: x * y, numbers)
    # 各桁の総和
    answer = reduce(lambda x, y: int(x) + int(y), str(target))

    print(answer) # answer 648

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.00019sec

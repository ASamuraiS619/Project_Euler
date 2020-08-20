# -*- coding: utf-8 -*-

'''
Problem63 「Powerful digit counts」

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
(n乗数になっているn桁の数字はいくつあるか。)
'''

# 10^(b-1) ≦ a^b < 10^bを満たせばよく、この不等式から1 ≦ a < 9が必要と分かる。
# 同じく上の不等式より、xの常用対数をlog10(x)と表すと、0 < b ≦ 1 / (1 - log10(a))となる。
# これを満たす整数bは全て条件を満たすのでその個数を足していく。

import time
from math import log10

if __name__ == '__main__':
    start = time.time()

    count = 0
    for a in range(1, 10):
        count += len(range(1, int(1 / (1 - log10(a)) + 1)))

    print(count)    # answer 49

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 10)) + "[sec]")   # 0.0000445843sec

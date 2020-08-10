# -*- coding: utf-8 -*-

'''
Problem53 「Combinatoric selections」

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation,(5 3) = 10.

In general, (n r) = n! / r!(n-r)!, where r≦ n, n! = n×(n-1)×…×3×2×1 , and 0! = 1 .

It is not until n=23, that a value exceeds one-million: (23 10) = 1144066.

How many, not necessarily distinct, values of (n r) for 1 ≦ n ≦ 100, are greater than one-million?
(1 ≦ n ≦ 100において、nCrが100万を超えるものはいくつあるか？(必ずしも値は区別しなくても良い。))
'''

import time
from math import factorial

# (2k 0)〜(2k k), (2k+1 0)〜(2k+1 k)までは単調増加、(n r) = (n n-r)なのでr'で100万を超えたとするとr'〜n-r'までは全て100万を超えている。

def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n-r))

if __name__ == '__main__':
    start = time.time()

    count = 0
    for n in range(1, 1001):
        for r in range(n // 2 + 1):
            if combination(n, r) > 10 ** 7:
                # (n-r') - r' + 1 = n-2r'+1
                count += n - 2 * r + 1
                break

    print(count)    # answer 4075

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 8)) + "[sec]")   # 0.0009532sec


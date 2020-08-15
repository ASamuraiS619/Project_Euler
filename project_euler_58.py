# -*- coding: utf-8 -*-

'''
Problem58 「Spiral primes」

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

[37] 36  35  34 33  32 [31]
 38 [17] 16  15 14 [13] 30
 39  18 [ 5]  4[ 3] 12  29
 40  19   6   1  2  11  28
 41  20 [ 7]  8  9  10  27
 42  21  22  23 24  25  26
[43] 44  45  46 47  48  49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
(螺旋状に数字を並べて正方形を作る時、両対角線上に含まれる素数の割合が対角線上の数字の個数の10%を下回る時の一辺の長さを求めよ。)
'''

import time
from functions import is_prime

if __name__ == '__main__':
    start = time.time()

    diagonals, prime_diagonals, prime_ratio, length = 1, 0, 1, 1
    while prime_ratio >= 0.1:
        length += 2
        diagonals += 4
        # length ** 2は素数にはなりえないので、判定から外す
        prime_diagonals += sum(map(is_prime, [length ** 2 - (length - 1) * i for i in [1, 2, 3]]))
        prime_ratio = prime_diagonals / diagonals

    print(length, diagonals, prime_diagonals, prime_ratio)   # answer 26241

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 2.2031sec

# -*- coding: utf-8 -*-

'''
Problem46 「Goldbach's other conjecture」

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
(素数と平方数の2倍の和で表せない最小の奇数は？)
'''

import time
from functions import is_prime

def as_conjectured(odd_num):
    flag = False
    for root in range(1, int(((odd_num - 3) / 2) ** 0.5) + 1):
        if (odd_num - 2 * root ** 2) in primes:
            flag = True
    return flag

if __name__ == '__main__':
    start = time.time()

    primes = set([2, 3, 5, 7])
    odd_num = 9
    while True:
        if is_prime(odd_num):
            primes.add(odd_num)
        else:
            if not as_conjectured(odd_num):
                print(odd_num)  # answer 5777
                break
        odd_num += 2

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.02985sec

# -*- coding: utf-8 -*-

'''
Problem47 「Distinct primes factors」

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
(４つの連続する数全てを4種の素数を組み合わせた積で表せるとき、一番最初の数を答えよ。)
'''

import time
from functions import is_prime

def has_four_distinct_prime_factors(num):
    distinct_prime_factors = []
    for prime in primes:
        if num == prime:
            distinct_prime_factors.append(prime)
            break
        elif num % prime == 0:
            distinct_prime_factors.append(prime)
            while num % prime == 0:
                num = num // prime
    if len(distinct_prime_factors) == 4:
        return True
    else:
        return False

def is_first_of_the_four_consecutive_integers(num):
    for number in range(num, num+4):
        if not has_four_distinct_prime_factors(number):
            return False
    return True

if __name__ == '__main__':
    start = time.time()

    target = 11
    # 何でも良いのだが、ひとまずこの4つだけ入れておく。
    primes = [2, 3, 5, 7]

    flag = False
    while flag == False:
        if is_prime(target):
            primes.append(target)
            diff = primes[-1] - primes[-2]
            if diff >= 5:
                for num in range(primes[-2] + 1, primes[-1] - 3):
                    if is_first_of_the_four_consecutive_integers(num):
                        print(num)  # answer 134043
                        flag = True
                        break
        target += 2


    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 4.40698sec

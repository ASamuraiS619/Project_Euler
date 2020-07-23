# -*- coding: utf-8 -*-

'''
Problem35 「Circular primes」

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
(100万以下の循環素数はいくつあるか。)
'''

import time
from functions import primes_up_to

def is_circular_prime(num):
    num_str = str(num)
    for i in range(len(num_str)):
        if int(num_str[i:] + num_str[:i]) not in target_primes_set:
            return False
    return True

if __name__ == '__main__':
    start = time.time()

    target_primes = primes_up_to(10 ** 6)
    target_primes_set = set(target_primes)

    circular_primes = set()
    for prime in target_primes:
        if is_circular_prime(prime):
            circular_primes.add(prime)

    print(len(circular_primes)) # answer 55

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 2.0001sec

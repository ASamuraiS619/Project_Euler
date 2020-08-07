# -*- coding: utf-8 -*-

'''
Problem50 「Consecutive prime sum」

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
(100万以下の素数の中で、最も長く連続した素数の和として表されるものを求めよ。)
'''

import time
from functions import is_prime

if __name__ == '__main__':
    start = time.time()

    # 2からの合計が100万を超えない、最長の素数リストを作る。
    target_primes = [2]
    target = 3
    _sum = 0
    while True:
        if is_prime(target):
            _sum += target
            if _sum > 10 ** 6:
                break
            else:
                target_primes.append(target)
        target += 2

    max_length = 0
    for start_index, start_prime in enumerate(target_primes):
        total = start_prime
        for end_index, end_prime in enumerate(target_primes[start_index + 1:]):
            total += end_prime
            length = end_index + 2
            if total > 10 ** 6:
                break
            elif is_prime(total) and length > max_length:
                max_length = length
                answer = total
    print(answer) # answer 997651

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.27459sec

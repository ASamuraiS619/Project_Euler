# -*- coding: utf-8 -*-

'''
Problem7 「10001番目の素数」

素数を小さい方から6つ並べると 2, 3, 5, 7, 11, 13 であり, 6番目の素数は 13 である.
10 001 番目の素数を求めよ.
'''
import time
from tqdm import tqdm

def is_prime(target, primes):
    for prime in primes:
        if target % prime == 0:
            return False
    return True

if __name__ == '__main__':
    start = time.time()

    prime_numbers = [2]
    target = 3
    with tqdm(total = 10000) as pbar:
        while True:
            if is_prime(target, prime_numbers):
                prime_numbers.append(target)
                pbar.update(1)
                if len(prime_numbers) == 10001:
                    print(target)   # answer 104743
                    break
            target += 2

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 2.33879sec

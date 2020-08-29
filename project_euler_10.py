# -*- coding: utf-8 -*-

'''
Problem10 「素数の和」

10以下の素数の和は 2 + 3 + 5 + 7 = 17 である.
200万以下の全ての素数の和を求めよ.
'''

import time

#エラトステネスの篩でnumber以下の素数を列挙
def primes_up_to(number):
    primes = set([i for i in range(3, number, 2)])
    tmp = set()
    while True:
        prime = min(primes)
        tmp.add(prime)
        if prime > number ** 0.5:
            primes = primes | tmp
            primes.add(2)
            return sorted(list(primes))
        else:
            primes = primes - set([i for i in range(prime, number, prime)])


if __name__ == '__main__':
    start = time.time()
    print(sum(primes_up_to(2 * 10 ** 6)))   # answer 142913828922
    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 3.48724sec

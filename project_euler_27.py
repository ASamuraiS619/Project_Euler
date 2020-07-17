# -*- coding: utf-8 -*-

'''
Problem27 「Quadratic primes」

Euler discovered the remarkable quadratic formula:
        n^2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,40^2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,41^2+41+41 is clearly divisible by 41.

The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n^2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
(n=0から始まる連続したnの値に対して最大数の素数を生成する2次式の係数aとbの積を求めよ。)
'''

import time

def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for divisor in range(3, int(num ** 0.5 + 1), 2):
            if num % divisor == 0:
                return False
        return True

def quadratic_formula_value(n, a, b):
    return n ** 2 + a * n + b

if __name__ == '__main__':
    start = time.time()

    # n=0のとき2次式の値はbとなり、それが素数なのでbは素数(かつ正の値)。
    # 1000以下の素数のリストを作成。bの候補となる。
    primes = []
    for i in range(1001):
        if is_prime(i):
            primes.append(i)

    max_times = 0
    for b in primes:
        # n=1のときを考えると、a<0ならaは最小でも-b+2
        for a in range(-b+2, 1001, 2):
            n = 0
            while True:
                if quadratic_formula_value(n, a, b) < 2:
                    break
                elif not is_prime(quadratic_formula_value(n, a, b)):
                    break
                else:
                    n += 1
            if n > max_times:
                combination = {'n':n, 'a': a, 'b':b}
                max_times = n

    print(combination['a'] * combination['b'])

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.53599sec


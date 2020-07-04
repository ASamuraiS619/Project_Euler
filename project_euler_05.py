# -*- coding: utf-8 -*-

'''
Problem5 「最小の倍数」

2520 は 1 から 10 の数字の全ての整数で割り切れる数字であり, そのような数字の中では最小の値である.
では, 1 から 20 までの整数全てで割り切れる数字の中で最小の正の数はいくらになるか.
'''

from sympy import sieve
from functools import reduce

def minimum_multiple(target):
    included_primes = sieve.primerange(1, target+1)

    # 素因数とtargetを超えない指数のセットを入れていく。
    prime_factorize_sets = []

    for prime in included_primes:

        # primeにべき乗してtargetを超えない指数を探しリストにしていく。
        # 最後にそれらのべき乗をかけ合わせれば求める答え。
        index = 1
        while True:
            if prime ** index > target:
                factor_set = [prime, index-1]
                break
            else:
                index += 1

        prime_factorize_sets.append(factor_set)

    # べき乗の配列に
    factors = map(lambda x: x[0] ** x[1], prime_factorize_sets)

    # 要素を全て掛け合わせる
    answer = reduce(lambda x, y: x * y, factors)

    return answer

if __name__ == '__main__':
    # answer 232792560
    print(minimum_multiple(20))

# -*- coding: utf-8 -*-

'''
Problem12 「高度整除三角数」

三角数の数列は自然数の和で表わされ, 7番目の三角数は 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28 である. 三角数の最初の10項は:
        1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
となる.
最初の7項について, その約数を列挙すると, 以下のとおり.
        1: 1
        3: 1,3
        6: 1,2,3,6
        10: 1,2,5,10
        15: 1,3,5,15
        21: 1,3,7,21
        28: 1,2,4,7,14,28
これから, 7番目の三角数である28は, 5個より多く約数をもつ最初の三角数であることが分かる.
では, 500個より多く約数をもつ最初の三角数はいくつか.
'''

from functions import primes_up_to
import time
import numpy as np

if __name__ == '__main__':
    start = time.time()

    n = 8
    while True:
        triangle_number = int(n * (n + 1) / 2)
        prime_factors = primes_up_to(int(triangle_number ** 0.5))
        # 素因数の最大指数を収納していく
        indexes = []
        for i in prime_factors:
            if triangle_number % i == 0:
                k = 1
                while True:
                    if triangle_number % (i ** k) != 0:
                        indexes.append(k-1)
                        break
                    else:
                        k += 1
        indexes_array = np.array(indexes)
        # 素因数の最大指数に全て1を足して掛け合わせると約数の総数が出る。
        if (indexes_array + 1).prod() > 500:
            print(triangle_number)  # answer 76576500
            break
        else:
            n += 1

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 3)) + "[sec]")   # 19.884sec

# -*- coding: utf-8 -*-

'''
Problem6 「二乗和の差」

最初の10個の自然数について, その二乗の和は,
        1^2 + 2^2 + ... + 10^2 = 385
最初の10個の自然数について, その和の二乗は,
        (1 + 2 + ... + 10)^2 = 3025
これらの数の差は 3025 - 385 = 2640 となる.
同様にして, 最初の100個の自然数について二乗の和と和の二乗の差を求めよ.
'''

import time

if __name__ == '__main__':
    start = time.time()

    numbers = list(range(1, 101))

    summation_of_square = sum(map(lambda x: x ** 2, numbers))
    square_of_summation = sum(numbers) ** 2

    diff = square_of_summation - summation_of_square

    # answer 25164150
    print(diff)

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 9)) + "[sec]")   # 0.000075102sec

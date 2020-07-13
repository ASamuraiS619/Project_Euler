# -*- coding: utf-8 -*-

'''
Problem23 「非過剰数和」

完全数とは, その数の真の約数の和がそれ自身と一致する数のことである. たとえば, 28の真の約数の和は, 1 + 2 + 4 + 7 + 14 = 28 であるので, 28は完全数である.

真の約数の和がその数よりも少ないものを不足数といい, 真の約数の和がその数よりも大きいものを過剰数と呼ぶ.

12は, 1 + 2 + 3 + 4 + 6 = 16 となるので, 最小の過剰数である. よって2つの過剰数の和で書ける最少の数は24である. 数学的な解析により, 28123より大きい任意の整数は2つの過剰数の和で書けることが知られている. 2つの過剰数の和で表せない最大の数がこの上限よりも小さいことは分かっているのだが, この上限を減らすことが出来ていない.

2つの過剰数の和で書き表せない正の整数の総和を求めよ.
'''

import time

if __name__ == '__main__':
    start = time.time()

    abundant_numbers = []
    # 最小の過剰数が12なので28123-12=28111まで。
    for num in range(28112):
        sum_of_divisors = 0
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                sum_of_divisors += i
                if i != 1 and num // i != i:
                    sum_of_divisors += int(num // i)
        if sum_of_divisors > num:
            abundant_numbers.append(num)

    sum_of_abundant_pair = []
    for i in range(len(abundant_numbers)):
        for k in range(i, len(abundant_numbers)):
            _sum = abundant_numbers[i] + abundant_numbers[k]
            if _sum <= 28123:
                sum_of_abundant_pair.append(_sum)
    # この後探索を行うので、setのままに。
    sum_of_abundant_pair = set(sum_of_abundant_pair)

    total = sum([num for num in range(28124) if num not in sum_of_abundant_pair])

    print(total) # answer 4179871

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 5.4287sec

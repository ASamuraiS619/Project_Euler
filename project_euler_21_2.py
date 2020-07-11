# -*- coding: utf-8 -*-

'''
Problem21 「友愛数」

d(n) を n の真の約数の和と定義する. (真の約数とは n 以外の約数のことである. )
もし, d(a) = b かつ d(b) = a (a ≠ b のとき) を満たすとき, a と b は友愛数(親和数)であるという.

例えば, 220 の約数は 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 なので d(220) = 284 である.
また, 284 の約数は 1, 2, 4, 71, 142 なので d(284) = 220 である.

それでは10000未満の友愛数の和を求めよ.
'''

import time

def divisors(num):
    divisors = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            # 平方根が含まれる場合は重複して数えないように。
            if i != 1 and num // i != i:
                divisors.append(int(num // i))
    return divisors

def d(n):
    return sum(divisors(n))

if __name__ == '__main__':
    start = time.time()

    total = 0
    for i in range(1, 10000):
        d_i = d(i)
        # d(a) = b かつ d(b) = a (a ≠ b のとき)なので a = bとなる場合は不可。
        if d_i <= 10000 and d_i != i and i == d(d_i):
            total += i

    print(total)    # answer 31262

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.08005sec

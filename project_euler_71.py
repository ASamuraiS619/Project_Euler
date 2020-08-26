# -*- coding: utf-8 -*-

'''
Problem71 「順序分数」

nとdを正の整数として, 分数 n/d を考えよう. n<d かつ HCF(n,d)=1 のとき, 真既約分数と呼ぶ.

d ≤ 8について既約分数を大きさ順に並べると, 以下を得る:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
3/7のすぐ左の分数は2/5である.

d ≤ 1,000,000について真既約分数を大きさ順に並べたとき, 3/7のすぐ左の分数の分子を求めよ.
'''

import time
from fractions import Fraction

def hcf(a, b):
    if a < b:
        a, b = b, a
    if a % b != 0:
        return hcf(b, a % b)
    else:
        return b

if __name__ == '__main__':
    start = time.time()

    answer = Fraction(2, 5)
    for d in range(9, 10 ** 6 + 1):
        for n in range(int(d * float(answer)), int(d * 3 / 7) + 1):
            if hcf(n, d) == 1 and Fraction(n, d) > answer:
                answer = Fraction(n, d)

    print(answer)   # answer 428570

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 4.15392sec

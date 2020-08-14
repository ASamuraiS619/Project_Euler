# -*- coding: utf-8 -*-

'''
Problem57 「Square root convergents」

It is possible to show that the square root of two can be expressed as an infinite continued fraction.
        √2 = 1 + 1 / (2 + 1 / (2 + 1/ (2 + 1/2+…)))
By expanding this for the first four iterations, we get:
        1 + 1/2 = 3/2 = 1.5
        1 + 1 / (2 + 1/2) = 7/5 = 1.4
        1 + 1 / (2 + 1 / (2 + 1/2)) = 17/12 = 1.41666…
        1 + 1 / (2 + 1 / (2 + 1/(2 + 1/2))) = 41/29 = 1.41379…

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?

(1000回展開を繰り返す中で、分子の桁数が分母の桁数よりも大きいものはいくつあるか。)
'''

import time
import sys
from fractions import Fraction

# n番目の展開についてf(n) = 1 + α(n)とすると、f(n+1) = 1 + 1 / (2 + α(n))となる。
# すなわちα(n+1) = 1 / (2 + α(n))
# α(n)のリストをfraction_sequenceと呼ぶこととする。
def fraction_sequence(length, sequence=[Fraction(1, 2)]):
    if len(sequence) == length:
        return sequence
    else:
        sequence.append(Fraction(1, 2 + sequence[-1]))
        return fraction_sequence(length, sequence)

def expansions(length):
    sequence = fraction_sequence(length)
    return list(map(lambda x: Fraction(1 + x), sequence))

if __name__ == '__main__':
    start = time.time()
    # 再帰上限数がデフォルトの1000では足りないので10000に書き換え。
    sys.setrecursionlimit(100000)

    LIM = 1000
    count = 0
    for expansion in expansions(LIM):
        if len(str(expansion.numerator)) > len(str(expansion.denominator)):
            count += 1

    print(count)    # answer 153

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.03605sec

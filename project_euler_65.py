# -*- coding: utf-8 -*-

'''
Problem65 「Convergents of e」

The square root of 2 can be written as an infinite continued fraction.

              1
√2 =  1 + --------------------------
                   1
             2 + ---------------------
                        1
                  2 + ----------------
                             1
                       2 + -----------
                                   1
                             2 + -----
                                  ...

The infinite continued fraction can be written, √2 = [1; (2)], (2) indicates that 2 repeats ad infinitum. In a similar way, √23 = [4; (1, 3, 1, 8)].

It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations. Let us consider the convergents for √2.

1 + 1/2 = 3/2

      1     7
1 + ----- = -
        1   5
    2 + -
        2

        1       17
1 + --------- = --
          1     12
    2 + -----
            1
        2 + -
            2

          1         41
1 + ------------- = --
            1       29
    2 + ---------
              1
        2 + -----
                1
            2 + -
                2

Hence the sequence of the first ten convergents for √2 are:

1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1939/985, 3363/2378, …

What is most surprising is that the important mathematical constant,
e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, … , 1, 2k, 1, … ].

The first ten terms in the sequence of convergents for e are:

2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, …

The sum of digits in the numerator of the 10th convergent is 1 + 4 + 5 + 7 = 17.

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
(e についての連分数である近似分数の100項目の分子の桁の合計を求めよ.)
'''

import time
from fractions import Fraction

def expandion_of_continued_fraction(continued_fraction_reversed_list, times=0, value=0):
    if times == len(continued_fraction_reversed_list):
        return value
    else:
        return expandion_of_continued_fraction(continued_fraction_reversed_list, times+1, Fraction(1, value + continued_fraction_reversed_list[times]))


if __name__ == '__main__':
    start = time.time()

    # eの連分数部分のみのリストを作成。
    e = [2 * ((num + 2) // 3) if num % 3 == 1 else 1 for num in range(99)]

    # 計算用に逆順に
    e.reverse()

    # 整数部分の2を足す。
    e_fraction = Fraction(2 + expandion_of_continued_fraction(e))

    print(sum(map(int, str(e_fraction.numerator))))     #answer 272
    print(float(e_fraction))

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 10)) + "[sec]")   # 0.0008568764sec

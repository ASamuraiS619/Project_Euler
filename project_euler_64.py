# -*- coding: utf-8 -*-

'''
Problem64 「Odd period square roots」

All square roots are periodic when written as continued fractions and can be written in the form:

           1
N = a0 + --------------------
                1
         a1 + ---------------
                     1
              a2 + ----------
                          1
                   a3 + -----
                         ...
For example, let us consider

                             1              1
√23 = 4 + 23 - 4 = 4 + ------------ = 4 + ---------------
                             1                 √23 - 3
                          --------         1 + --------
                          √23 - 4                  7
If we continue we would get the following expansion:
              1
√23 =  4 + --------------------------
                   1
             1 + ---------------------
                        1
                  3 + ----------------
                             1
                       1 + -----------
                                   1
                             8 + -----
                                  ...
The process can be summarised as follows:

a0 = 4, 1/(√23-4) =  (√23+4)/7  = 1 + (√23-3)/7
a1 = 1, 7/(√23-3) = 7(√23+3)/14 = 3 + (√23-3)/2
a2 = 3, 2/(√23-3) = 2(√23+3)/14 = 1 + (√23-4)/7
a3 = 1, 7/(√23-4) = 7(√23+4)/7  = 8 + (√23-4)
a4 = 8, 1/(√23-4) =  (√23+4)/7  = 1 + (√23-3)/7
a5 = 1, 7/(√23-3) = 7(√23+3)/14 = 3 + (√23-3)/2
a6 = 3, 2/(√23-3) = 2(√23+3)/14 = 1 + (√23-4)/7
a7 = 1, 7/(√23-4) = 7(√23+4)/7  = 8 + (√23-4)

It can be seen that the sequence is repeating. For conciseness, we use the notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.

The first ten continued fraction representations of (irrational) square roots are:

√2=[1;(2)], period=1
√3=[1;(1,2)], period=2
√5=[2;(4)], period=1
√6=[2;(2,4)], period=2
√7=[2;(1,1,1,4)], period=4
√8=[2;(1,4)], period=2
√10=[3;(6)], period=1
√11=[3;(3,6)], period=2
√12= [3;(2,6)], period=2
√13=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N ≦ 13, have an odd period.

How many continued fractions for N ≦ 10000 have an odd period?
'''

import time

# a / (√b - c)の形の分数を(a, b, c)で渡し、次の分数を同じくタプルの形で返す。
def next_fraction(fraction):
    a, b, c = fraction
    # 約分できてしまう場合
    if (b - c ** 2) % a == 0:
        numerator = b ** 0.5 + c
        denominator = (b - c ** 2) // a
    else:
        numerator = a * (b ** 0.5 + c)
        denominator = b - c ** 2
    integer = int(numerator / denominator)
    return (denominator, b, -(c - denominator * integer))

# 最初の値と同じ分数が出てきたらそれ以降循環するので、その時点でperiodを計算して返す。
def continued_fraction_period(square_root_content, sequence):
    if len(sequence) == 0:
        sequence.append((1, square_root_content, int(square_root_content ** 0.5)))
        return continued_fraction_period(square_root_content, sequence)

    if len(sequence) != 1 and sequence[-1] == sequence[0]:
        return len(sequence) - 1
    else:
        sequence.append(next_fraction(sequence[-1]))
        return continued_fraction_period(square_root_content, sequence)

if __name__ == '__main__':
    start = time.time()

    count = 0
    for num in range(2, 10001):
        if (num ** 0.5).is_integer():
            continue
        elif continued_fraction_period(num, []) % 2 == 1:
            count += 1

    print(count)    # answer 1322

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.3543sec

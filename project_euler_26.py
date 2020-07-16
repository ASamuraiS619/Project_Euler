# -*- coding: utf-8 -*-

'''
Problem26 「Reciprocal cycles」

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
(1000以下の分母からなる単位分数で、最も長い繰り返し部分となるものを答えよ。)
'''

import time

def recurring_cycle_digit(d, numerator=1, digits=0):
    if d != 2 and d % 2 == 0:
        return recurring_cycle_digit(d // 2, numerator, digits)
    elif d != 5 and d % 5 == 0:
        return recurring_cycle_digit(d // 5, numerator, digits)
    else:
        mod = (numerator * 10) % d
        digits += 1
        if mod == 0:
            return 0
        elif mod == 1:
            return digits
        else:
            return recurring_cycle_digit(d, mod, digits)


if __name__ == '__main__':
    start = time.time()

    answer = None
    max_digits = 0
    for d in range(1, 1000):
        digits = recurring_cycle_digit(d)
        if digits > max_digits:
            answer = d
            max_digits = digits
    print(answer)   # answer 983

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.03153sec


# -*- coding: utf-8 -*-

'''
Problem48 「Self powers」

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
(1^1 + 2^2 + 3^3 + ... + 1000^1000の下10桁を答えよ。)
'''

import time

if __name__ == '__main__':
    start = time.time()

    _sum = sum([num ** num for num in range(1, 1001)])
    print(str(_sum)[-10:])  # answer 9110846700

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.00917sec

# -*- coding: utf-8 -*-

'''
Problem1 「3と5の倍数」

10未満の自然数のうち, 3 もしくは 5 の倍数になっているものは 3, 5, 6, 9 の4つがあり, これらの合計は 23 になる.
同じようにして, 1000 未満の 3 か 5 の倍数になっている数字の合計を求めよ.
'''

import time

if __name__ == '__main__':
    start = time.time()
    proper_numbers = [num for num in range(1, 1000) if num % 3 == 0 or num % 5 == 0]

    # answer 233168
    print(sum(proper_numbers))

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.00014sec

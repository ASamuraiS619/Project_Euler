# -*- coding: utf-8 -*-

'''
Problem76 「和の数え上げ」

5は数の和として6通りに書くことができる:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

2つ以上の正整数の和としての100の表し方は何通りか.
'''

import time

if __name__ == '__main__':
    start = time.time()

    summetion_count_dict = {1: [0], 2: [1]}

    for n in range(3, 101):
        summetion_count_dict[n] = []
        for a in range(n-1, 0, -1):
            b = n - a
            if a >= b:
                summetion_count_dict[n].append(1 + sum(summetion_count_dict[b]))
            else:
                summetion_count_dict[n].append(sum(summetion_count_dict[b][-a:]))

    print(sum(summetion_count_dict[100]))   # answer 190569291

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.00337sec

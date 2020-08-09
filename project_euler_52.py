# -*- coding: utf-8 -*-

'''
Problem52 「Permuted multiples」

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
(2x, 3x, 4x, 5x, 6xが同じ数字を含むような最小の正の整数xを求めよ。)
'''

# 6倍しても桁数が変わらないので10XXX〜(10XXXX / 6)までに答えがある。

import time

if __name__ == '__main__':
    start = time.time()

    index_number = 1
    flag = False
    while flag == False:
        for num in range(10 ** index_number, int(10 ** (index_number+1) / 6 + 1)):
            if set(str(num)) == set(str(num * 2)) == set(str(num * 3)) == set(str(num * 4)) == set(str(num * 5)) == set(str(num * 6)):
                print(num)  # answer 142857
                flag = True
                break
        index_number += 1

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.056sec

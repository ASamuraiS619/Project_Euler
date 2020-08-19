# -*- coding: utf-8 -*-

'''
Problem62 「Cubic permutations」

The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
(桁を並び替えると他に4つの立方数となる、最小の立方数を求めよ。)
'''

import time

def digits_tuple(num):
    digits = {}
    str_num = str(num)
    for digit_number in str_num:
        try:
            digits[digit_number] += 1
        except KeyError:
            digits[digit_number] = 1
    # タプルでないと辞書のキーに出来ないのでタプル化して返す。
    return tuple(sorted(digits.items()))

if __name__ == '__main__':
    start = time.time()

    digits_of_cubes = {}
    num = 1
    while True:
        cube = num ** 3
        try:
            digits_of_cubes[digits_tuple(cube)].append(cube)
        except KeyError:
            digits_of_cubes[digits_tuple(cube)] = [cube]
        if len(digits_of_cubes[digits_tuple(cube)]) == 5:
            print(min(digits_of_cubes[digits_tuple(cube)])) # answer 127035954683
            break
        else:
            num += 1

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.09943sec

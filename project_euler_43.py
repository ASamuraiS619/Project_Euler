# -*- coding: utf-8 -*-

'''
Problem43 「Sub-string divisibility」

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d(1) be the 1st digit, d(2) be the 2nd digit, and so on. In this way, we note the following:

①d(2)d(3)d(4)=406 is divisible by 2
②d(3)d(4)d(5)=063 is divisible by 3
③d(4)d(5)d(6)=635 is divisible by 5
④d(5)d(6)d(7)=357 is divisible by 7
⑤d(6)d(7)d(8)=572 is divisible by 11
⑥d(7)d(8)d(9)=728 is divisible by 13
⑦d(8)d(9)d(10)=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
(0〜9のパンデジタル数で、上からn桁目の数をd(n)とするとき①〜⑦の性質を持つものを全ての合計を求めよ。)
'''

import time
from itertools import permutations

def has_property(number_str):
    if number_str[0] == '0':
        return False
    for index, prime in enumerate(PRIME_NUMBERS):
        sliced_number = int(number_str[index + 1: index + 4])
        if sliced_number % prime != 0:
            return False
    return True

if __name__ == '__main__':
    start = time.time()

    PRIME_NUMBERS = [2, 3, 5, 7, 11, 13, 17]

    # permutationsを使って、まずは順列(タプル)のリストを作成
    pandigital_numbers = list(permutations([str(num) for num in range(10)]))
    # タプルを結合して数値化
    pandigital_numbers = list(map(lambda x: ''.join(x), pandigital_numbers))

    _sum = 0
    for number_str in pandigital_numbers:
        if has_property(number_str):
            _sum += int(number_str)

    print(_sum)

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 4.13341sec

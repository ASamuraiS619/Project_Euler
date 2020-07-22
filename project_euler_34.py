# -*- coding: utf-8 -*-

'''
Problem34 「Digit factorials」

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
(各桁の階乗の和がその数そのものと等しくなる数の合計を求めよ。)
'''

import time
from functools import reduce

def is_the_curious_number(num):
    if num <= 2:
        return False
    else:
        sum_of_digit_factorials = sum(map(lambda x: factorials[x], str(num)))
        if sum_of_digit_factorials == num:
            return True
        else:
            return False

if __name__ == '__main__':
    start = time.time()

    # 階乗の辞書を作っておく。0!=1だけ先に入れておく。
    factorials = {'0': 1}
    for i in range(1, 10):
        factorials[str(i)] = reduce(lambda x, y: x * y, range(i, 0, -1))

    # すべての桁が9だとして、9! = 362880から、 362880 * 8 = 2903040なので該当するとしたら7桁未満。
    # もっというと 9!*3 + 1!*4 = 1088644以下。
    the_curious_numbers = []
    for num in range(factorials['9'] * 3 + 5):
        if is_the_curious_number(num):
            the_curious_numbers.append(num)

    print(the_curious_numbers)
    print(sum(the_curious_numbers))

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 1.27295sec

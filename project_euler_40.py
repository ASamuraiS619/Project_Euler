# -*- coding: utf-8 -*-

'''
Problem40 「Champernowne's constant」

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.
If d(n) represents the nth digit of the fractional part, find the value of the following expression.

d(1) × d(10) × d(100) × d(1000) × d(10000) × d(100000) × d(1000000)
(チャンパーノウン定数の小数第n位の数をd(n)とするとき、d(1) × d(10) × d(100) × d(1000) × d(10000) × d(100000) × d(1000000)の値を求めよ。)
'''

import time

def d(n):
    if n < 10:
        return n

    # n桁目が何桁の数の一部なのかを調べる
    # index = 3であれば100〜999の数の一部
    index = 1
    digit = 0
    while True:
        if digit + monopolizing_length_dict[index] > n:
            break
        else:
            digit += monopolizing_length_dict[index]
            index += 1

    # (index)桁の数の「何番目」の数字の「何文字目」かを求めて返す。
    # (left_digits // index) + 1が上記の「何番目」に該当
    # left_digits % indexが上記の「何文字目」に該当
    left_digits = n - digit
    return int(str(range(10 ** (index - 1), 10 ** index)[left_digits // index])[left_digits % index - 1])

if __name__ == '__main__':
    start = time.time()

    THRESHOLD = 10 ** 6

    # 何桁の線数桁数まで辞書に入れるべきかを計算(dict_digit)
    dict_digit = 0
    sum_of_digit = 0
    while True:
        if sum_of_digit > THRESHOLD:
            break
        else:
            dict_digit += 1
            sum_of_digit = dict_digit * 9  * 10 ** (dict_digit - 1)

    # 1桁の数字(1〜9)、2桁の数字(10〜99)で何桁専有しているかを辞書に。
    # n桁の場合、n * (10^n - 10^(n-1)) = n * 9 * 10^(n-1)
    monopolizing_length_dict = {index: index * 9  * 10 ** (index - 1) for index in range(1, dict_digit + 1)}

    answer = 1
    for index_of_ten in range(7):
        print(d(10 ** index_of_ten))
        answer *= d(10 ** index_of_ten)

    print(answer)   # answer 210

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.00012sec
